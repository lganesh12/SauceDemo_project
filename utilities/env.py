import os

from dotenv import load_dotenv

from features.variable import PROJECT_ROOT


def load_env():
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(dotenv_path=env_path)


def get_env_value(name):
    value = os.getenv(name)
    if value is None:
        raise KeyError(f"Environment variable {name} not found.")
    return value


def is_truthy(bool_as_string: str):
    bool_as_string = {"1": "true", "0": "false"}.get(bool_as_string, bool_as_string)
    return bool_as_string.lower() == "true"


def fail(msg=""):
    """Force test failure with the given message.

    :param msg: str
    """
    raise AssertionError(f"Fail: {msg}!" if msg else "Fail!")


def set_context_var(context, var, value, level="scenario"):
    """Set variable in context.

    :param context: context object
    :type context: behave.runner.Context
    :param var: variable
    :type var: str
    :param value: value to be set
    :type level: feature tag or scenario
    :param level: str
    """
    if level == "scenario":
        context.vars[var] = value
    elif level == "tag":
        context.tag_vars[var] = value
    else:
        fail(f"Level {level} defined is invalid.")


def get_context_var(context, var, fail=False, level="scenario"):
    """Get variable from context.

    :param context: context object
    :type context: behave.runner.Context
    :param var: variable
    :type var: str
    :param fail: true or false : is set then Keyerror should be thrown if variable not found.
    :type fail: boolean
    :param level: feature tag or scenario
    :type level: str
    """
    if level == "scenario" and fail:
        return context.vars[var]
    elif level == "tag" and fail:
        return context.tag_vars[var]
    else:
        return context.vars.get(var, var)
