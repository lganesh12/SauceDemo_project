from behave import given
from behave import use_step_matcher


use_step_matcher("re")


@given("the user is on the SauceDemo login page")
def do_nothing(context):
    """Do nothing in this step
    :param context: behave context.
    :type context: behave.runner.Context
    """
    pass
