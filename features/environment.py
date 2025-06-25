from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import fixture
from behave import use_fixture
from behave.model_core import Status
from playwright.sync_api import sync_playwright
from features.variable import SLOW_MOTION_TIME
from user_flow.user import User
from utilities.env import get_env_value
from utilities.env import is_truthy
from utilities.env import load_env



def setup_browser(context, playwright, storage_state=False):
    """Setup browser with capabilities.

    :param context: context object
    :type context: behave.runner.Context
    :param storage_state: User storage state for login
    :type storage_state: bool
    """
    if context.browser == "Chrome":
        browser = playwright.chromium.launch(
            headless=context.headless,
            slow_mo=SLOW_MOTION_TIME,

            args=["--disable-blink-features=AutomationControlled"],
        )
    elif context.browser == "Firefox":
        browser = playwright.firefox.launch(
            headless=context.headless,
            slow_mo=SLOW_MOTION_TIME,
        )
    context.browser_context = browser.new_context()
    context.page = context.browser_context.new_page()
    return context.browser_context, context.page


@fixture
def setup_playwright(context, storage_state=False):
    """Fixture to setup the playwright before test execution.

    :param context: context object
    :type context: behave.runner.Context
    :param storage_state: User storage state for login
    :type storage_state: bool
    """
    # -- SETUP-FIXTURE PART:
    context.playwright = sync_playwright().start()

    browser, context.page = setup_browser(
        context, context.playwright, storage_state
    )
    yield context.page
    # -- CLEANUP-FIXTURE PART:
    browser.close()
    context.playwright.stop()


def before_all(context):
    """Before all hook to run at start of test execution.

    :param context: behave.runner.Context
    :type context: behave.runner.Context
    """
    load_env()
    context.browser = get_env_value("BROWSER")
    context.headless = is_truthy(get_env_value("HEADLESS"))
    context.base_url = get_env_value("BASE_URL")
    context.password = get_env_value("PASSWORD")
    context.username = get_env_value("USERNAME")
    use_fixture(setup_playwright, context, storage_state=True)
    context.page.goto(context.base_url, wait_until="load", timeout=60000)



def before_scenario(context, scenario):
    context.user = User(context.page, context, "standard_user", "secret_sauce")


def after_scenario(context, scenario):
    """Attach a screenshot and browser console logs if scenario is failed.

    :param context: behave.runner.Context
    :type context: behave.runner.Context
    :param scenario: behave scenario
    :type context: behave.model.Scenario
    """

    if scenario.status == Status.failed:
        #Screenshot
        attach(context.page.screenshot(),name=f"Screenshot : {scenario.name}",attachment_type=AttachmentType.PNG)
    else:
        context.user.logout()


