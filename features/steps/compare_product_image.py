import logging
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

from behave import given
from behave import then
from behave import use_step_matcher
from behave import when

from features.locators import dict_locators
from features.variable import PROJECT_ROOT
from utilities.env import image_comparison

use_step_matcher("re")


@given("the user is logged wants to verify product image matches baseline image")
def user_login(context):
    """User login to application
    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.user.login()


@when("the user navigates to the product details page for Sauce Labs Bolt T-Shirt")
def user_navigate_to_product_detail_page(context):
    """User navigates to product detail page
    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.page.locator(dict_locators["product_name"]).click()
    img_locator = context.page.locator("img.inventory_details_img")
    img_locator.wait_for(state="visible")
    relative_img_path = img_locator.get_attribute("src")
    if not relative_img_path:
        raise ValueError("Image source not found in the DOM")
    base_url = context.page.url.split("/product")[0]
    absolute_img_url = urljoin(base_url, relative_img_path)
    download_dir = Path(PROJECT_ROOT) / "image_comparison" / "test_image"
    download_dir.mkdir(parents=True, exist_ok=True)
    download_path = download_dir / "test_image.jpg"
    try:
        urllib.request.urlretrieve(absolute_img_url, str(download_path))
        logging.info(f"Image successfully downloaded to: {download_path}")
    except Exception as e:
        logging.error(f"Error downloading image: {e}")
        raise


@then("the product image should match the baseline image")
def Validate_product_image(context):
    """User navigates to product detail page
    :param context: behave context.
    :type context: behave.runner.Context
    """
    base_image_path = (
        PROJECT_ROOT / "image_comparison" / "base_image" / "base_image.jpg"
    )
    test_image_path = (
        PROJECT_ROOT / "image_comparison" / "test_image" / "test_image.jpg"
    )
    image_comparison_status = image_comparison(base_image_path, test_image_path)
    assert image_comparison_status, " Base Image and Test Image do not match"
