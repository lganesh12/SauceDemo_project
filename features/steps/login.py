from behave import given
from behave import then
from behave import use_step_matcher
from behave import when
from playwright.sync_api import expect

from features.locators import dict_locators

use_step_matcher("re")


@given("the user is on the SauceDemo login page")
def do_nothing(context):
    """Do nothing in this step
    :param context: behave context.
    :type context: behave.runner.Context
    """
    pass


@when("the user enters (?P<username>.+) and (?P<password>.+)")
def user_enters_login_credentials(context, username, password):
    """User Enter login credentials
    :param context: behave context.
    :type context: behave.runner.Context
    :param username: username
    :type username: str
    :param password: password
    :type password: str
    """
    context.user.enter_text(dict_locators["username_text_box"], username)
    context.user.enter_text(dict_locators["password_text_box"], password)


@when("he clicks the login button")
def user_click_on_login_button(context):
    """user click on the login button
    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.user.click_btn(dict_locators["login_button"])


@then("the user should (?P<expected_result>.+)")
def verify_user_get_expected_result(context, expected_result):
    """Verify user get expected result
    :param context: behave context.
    :type context: behave.runner.Context
    :param expected_result: expected_result
    :type expected_result: str
    """
    if expected_result == "the Products page is displayed":
        locator = context.page.locator(dict_locators["title_page"])
        expect(locator).to_have_text("Products")
    elif expected_result == "an error message is displayed":
        pass
    elif expected_result == "the locked out error appears":
        pass
    elif expected_result == "the username required error appears":
        pass
    elif expected_result == "the password required error appears":
        pass
    else:
        pass
