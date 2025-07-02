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
