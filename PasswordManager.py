import string
import random

import yaml


def get_password_file():
    return open("cache/password.yaml", 'a+')


def get_password_content():
    return open("cache/password.yaml", "r+")


def get_random_password(length: int = 16):
    result = ""
    main_list = string.ascii_letters + string.punctuation + string.digits
    for _ in range(length):
        index = random.randint(0, len(main_list) - 1)
        result += main_list[index]

    return result


def register_password(application_name: str, password: str):
    insertion = [{application_name.lower(): "\"" + password + "\""}]
    yaml.dump(insertion, get_password_file())


def get_all_applications():
    yaml_file = yaml.safe_load(get_password_content())
    applications = []

    if yaml_file is not None:
        for dictionary in yaml_file:
            for key, value in dictionary.items():
                applications.append(key)

    return applications


def contain_app(application: string):
    contain = False
    for applications in get_all_applications():
        if applications == application:
            contain = True

    return contain
