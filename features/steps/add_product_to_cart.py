from behave import *

from features.locators import dict_locators
from user_flow.user import User

use_step_matcher("re")


@given("the user is wants to Add a product to the shopping cart")
def login_as_admin(context):
    """Login as admin

    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.user = User(context.page, context, "standard_user", "secret_sauce")
    context.user.login()


@when('the user adds the product "Sauce Labs Backpack" to the cart')
def user_add_product_to_cart(context):
    """User add product to cart

    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.page.locator(dict_locators["Sauce_Labs_Backpack"]).click()
    context.user.click_btn(dict_locators["Add_to_cart"])


@then("the shopping cart icon should show 1 item")
def verify_shopping_cart_should_show_item(context):
    """Verify the shopping cart icon should show added item

    :param context: behave context.
    :type context: behave.runner.Context
    """
    total_item_added_in_cart = context.page.locator(dict_locators["item_added_in_cart"]).text_content()
    print("total_item_added_in_cart",total_item_added_in_cart)