import atexit
import string
import time

import yaml
import logging


class Logs:

    def __init__(self, file_path: str):
        self.logging = logging
        self.file_path = file_path
        self.logging.basicConfig(filename=file_path, format='%(asctime)s | %(levelname)s: %(message)s',
                                 datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)

    def error(self, message: str):
        self.logging.error(message)
        write_console(message, "ERROR")

    def critical(self, message: str):
        self.logging.critical(message)
        write_console(message, "CRITICAL")

    def warning(self, message: str):
        self.logging.warning(message)
        write_console(message, "WARNING")

    def information(self, message: str):
        self.logging.info(message)
        write_console(message, "INFO")

    def clear(self):
        open(self.file_path, "w")
        self.logging.warning("Starting logging recorder...")

    def exit_handler(self):
        self.logging.warning(f"Stopping '{self.file_path}' recorder...")


class YamlFile:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_yaml_file(self):
        return open(self.file_path, 'a+')

    def get_yaml_content(self):
        return open(self.file_path, "r+")

    def get_key(self, target_key: str):
        yaml_file = yaml.safe_load(self.get_yaml_content())
        if yaml_file is not None:
            for dictionary in yaml.safe_load(self.get_yaml_content()):
                for key, value in dictionary.items():
                    if key.lower() == target_key.lower():
                        return value

        return None

    def register_key(self, key: str, value, logs=None):
        insertion = [{key: value}]
        if self.contain_key(key):
            logs.warning(f"Replacing '{key}' value to '{value}' in '{self.file_path}'")
            self.remove_key(key)
        yaml.dump(insertion, self.get_yaml_file())

    def get_all_keys(self):
        yaml_file = self.get_yaml_content()
        keys = []
        if yaml_file is not None:
            for dictionary in yaml.safe_load(self.get_yaml_content()):
                for key, value in dictionary.items():
                    keys.append(key)

        return keys

    def remove_key(self, target_key: string):
        yaml_file = yaml.safe_load(self.get_yaml_content())
        new_file = open(self.file_path, "w+")
        dictionary_list = []
        for dictionary in yaml_file:
            for key, value in dictionary.items():
                if key != target_key:
                    dictionary_list.append(dictionary)
        if len(dictionary_list) != 0:
            yaml.dump(dictionary_list, new_file)

    def contain_key(self, target_key: string):
        contain = False
        for key in self.get_all_keys():
            if key == target_key:
                contain = True

        return contain

    def create_file(self, dictionary_list=None, logs=None):
        try:
            file = open(self.file_path, 'r+')
        except Exception:
            file = open(self.file_path, 'a+')
            yaml.dump(dictionary_list, file)
            logs.warning(f"Can't find '{self.file_path}', creating one")



def write_console(message, level):
    print(time.strftime('%m/%d/%Y %I:%M:%S %p', time.localtime()), "|", level + ":", message)
