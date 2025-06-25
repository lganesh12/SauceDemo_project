import logging

from behave import *
from playwright.sync_api import expect

from features.locators import dict_locators
from user_flow.user import User

use_step_matcher("re")


@given("the user is on the SauceDemo login page")
def do_nothing(context):
    """Do nothing in this step
    :param context: behave context.
    :type context: behave.runner.Context
    """
    pass


@when("the user enters (?P<condition>valid|invalid) login credentials")
def user_enter_valid_credentials(context,condition):
    """User enters valid login credentials

    :param context: behave context.
    :type context: behave.runner.Context
    :param condition: valid or invalid
    :type condition: str
    """
    context.user = User(context.page, context, "standard_user", "secret_sauce")
    if condition == "valid":
        context.user.enter_text(dict_locators["username_text_box"], "standard_user")
        context.user.enter_text(dict_locators["password_text_box"], "secret_sauce")
    elif condition == "invalid":
        context.user.enter_text(dict_locators["username_text_box"], "standad_user")
        context.user.enter_text(dict_locators["password_text_box"], "secret_sauc")
    else:
        logging.info("Invalid credentials entered")




@step("he clicks the login button")
def user_click_login_button(context):
    """User click login button

    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.user.click_btn(dict_locators["login_button"])


@then("the Products page is displayed")
def verify_display_of_product_page(context):
    """Verify product page is displayed

    :param context: behave context.
    :type context: behave.runner.Context
    """
    try:
        assert context.page.locator("//*[@class='title']").text_content() == "Products"
    except Exception as e:
        raise AssertionError("The product page is not displayed") from e


@then("he see an error message is displayed")
def verify_an_error_message_for_invalid_credentials(context):
    """Verify an error message is displayed for invalid credentials

    :param context: behave context.
    :type context: behave.runner.Context
    """
    error_message = "Epic sadface: Username and password do not match any user in this service"
    expect(context.page.locator("//h3[@data-test='error']")).to_have_text(error_message)


@then("he remains on the login page")
def verify_user_remain_on_login_page_for_invalid_credentials(context):
    """Verify user remain on login page for invalid credentials

    :param context: behave context.
    :type context: behave.runner.Context
    """
    assert context.page.is_visible("#login_credentials")