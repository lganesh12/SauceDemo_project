import logging

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import fixture
from behave import use_fixture
from behave.model_core import Status
from playwright.sync_api import sync_playwright

from features.locators import dict_locators
from features.variable import ELEMENT_WAIT_TIME
from features.variable import SLOW_MOTION_TIME
from user_flow.user import User
from utilities.env import get_env_value
from utilities.env import is_truthy
from utilities.env import load_env

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("test_execution.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def setup_browser(context, playwright, storage_state=False):
    """Setup browser with capabilities."""
    logger.info(f"Setting up {context.browser} browser")

    if context.browser == "Chrome":
        browser = playwright.chromium.launch(
            headless=context.headless,
            slow_mo=SLOW_MOTION_TIME,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-blink-features",
                "--ignore-certificate-errors",
            ],
        )
    elif context.browser == "Firefox":
        browser = playwright.firefox.launch(
            headless=context.headless,
            slow_mo=SLOW_MOTION_TIME,
        )
    context.browser_context = browser.new_context()
    context.page = context.browser_context.new_page()
    logger.info(f"Browser setup completed for {context.browser}")
    return context.browser_context, context.page


@fixture
def setup_playwright(context, storage_state=False):
    """Fixture to setup the playwright before test execution."""
    logger.info("Starting Playwright setup")
    context.playwright = sync_playwright().start()

    browser, context.page = setup_browser(context, context.playwright, storage_state)
    yield context.page

    logger.info("Cleaning up Playwright resources")
    browser.close()
    context.playwright.stop()


def before_all(context):
    """Before all hook to run at start of test execution."""
    logger.info("Test execution started")
    load_env()
    context.browser = get_env_value("BROWSER")
    context.headless = is_truthy(get_env_value("HEADLESS"))
    context.base_url = get_env_value("BASE_URL")
    context.password = get_env_value("PASSWORD")
    context.username = get_env_value("USERNAME")


def before_scenario(context, scenario):
    """Log scenario start and initialize user."""
    logger.info(f"Starting scenario: {scenario.name}")
    logger.info(f"Tags: {', '.join(scenario.tags)}")
    logger.info(
        f"Environment loaded - Browser: {context.browser}, Headless: {context.headless}, Base URL: {context.base_url}"
    )

    use_fixture(setup_playwright, context, storage_state=True)
    logger.info(f"Navigating to base URL: {context.base_url}")
    context.page.goto(context.base_url, wait_until="load", timeout=1200000)
    context.user = User(context.page, context, context.username, context.password)
    logger.info("User initialized")


def after_scenario(context, scenario):
    """Log scenario completion and attach artifacts if failed."""
    logger.info(
        f"Scenario '{scenario.name}' completed with status: {scenario.status.name}"
    )

    # Attach screenshot and logs if scenario failed
    if scenario.status == Status.failed:
        logger.error(
            f"Scenario failed! Attaching screenshot and logs for {scenario.name}"
        )
        attach(
            context.page.screenshot(),
            name=f"Screenshot : {scenario.name}",
            attachment_type=AttachmentType.PNG,
        )
        console_logs = context.page.evaluate(
            "() => {return JSON.stringify(console.logs);}"
        )
        if console_logs:
            attach(
                console_logs,
                name="Browser Console Logs",
                attachment_type=AttachmentType.TEXT,
            )

    # Only attempt logout if:
    # 1. The scenario passed (no need to check in failed cases)
    # 2. The user is on a page where logout is possible (e.g., not on login page)
    elif hasattr(context, "page") and not context.page.url.endswith("/inventory.html"):
        try:
            if context.page.locator(dict_locators["burger_menu_btn"]).is_visible(
                ELEMENT_WAIT_TIME
            ):
                logger.info("Logging out user after successful scenario")
                context.user.logout()
        except Exception as e:
            logger.debug(
                f"Skipping logout (user not logged in or already logged out): {e}"
            )

    # Always close the page
    if hasattr(context, "page"):
        context.page.close()
