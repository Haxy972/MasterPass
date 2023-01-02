import string
import random

import Display
from Utils import Logs, YamlFile
from Display import ConditionsWindow, AppWindow
import atexit


def get_random_password(length: int = 16):
    result = ""
    main_list = string.ascii_letters + string.punctuation + string.digits
    for _ in range(length):
        index = random.randint(0, len(main_list) - 1)
        result += main_list[index]

    return result


def get_logs():
    return logs


def get_settings_file():
    return settings_file


def launch_app():
    if not get_settings_file().get_key("approve_conditions"):
        Display.launch_condition_window()
    else:
        Display.launch_app_window()


def exit_handler():
    logs.warning("Stopping logs recorder...")


atexit.register(exit_handler)
logs = Logs("latest.log")
logs.clear()
settings_file = YamlFile("cache/settings.yaml")
default_settings = [{'approve_conditions': False}]
settings_file.create_file(default_settings, logs)
launch_app()
