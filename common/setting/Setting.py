from configparser import ConfigParser
import os

class Setting:
    """
    This class instanse handle setting.
    ■read method
    the read method is show setting.
    this method receive one args that is tuple.
    the tuple is the sections of a setting.

    ■write method
    the write method write setting.
    this method receive one args that is tuple and one arg anytype.
    the tuple args is the sections of a setting.
    the anytype arg is value of write.
    """
    FILE_NAME = "setting.ini"
    CONFIG_FILE_PATH = os.path.join("setting", FILE_NAME)
    TUPLE_SEP = "/"
    SECTION_NAME_FLG = None
    SECTION_EXPLAIN_NAME = "explain"

    @classmethod
    def config_load(cls):
        cls.common_config:ConfigParser = ConfigParser()
        dir_name = os.path.dirname(__file__)
        path = os.path.join(dir_name, cls.FILE_NAME)
        cls.common_config.read(path)
        cls.config:ConfigParser = ConfigParser()
        cls.config.read(cls.CONFIG_FILE_PATH)

    @classmethod
    def config_reset(cls):
        cls.config_load()

    @classmethod
    def config_save(cls):
        with open(cls.CONFIG_FILE_PATH, mode="w") as config_file:
            cls.config.write(config_file)

    @classmethod
    def common_config_dict(cls):
        try:
            cls.common_config
        except AttributeError:
            cls.config_load()
        return cls.config_iterater(cls.common_config)

    @classmethod
    def read(cls, section, key, is_tuple=False, default=None):
        section = str(section)
        key = str(key)
        try:
            sec = cls.config[str(section)]
        except AttributeError:
            cls.config_load()
            return cls.read(section, key, is_tuple=is_tuple, default=default)
        except KeyError:
            return default

        value:str = sec.get(str(key), default)
        if is_tuple and value:
            return tuple(value.split(cls.TUPLE_SEP))
        else:
            return value

    @classmethod
    def write(cls, section, key, value="", is_tuple=False):
        try:
            cls.config
        except AttributeError:
            return cls.write(section, key, value=value, is_tuple=is_tuple)

        section = str(section)
        key = str(key)
        value = str(value)
        if section not in cls.config:
            cls.config[section] = {}

        if is_tuple:
            cls.config[section][key] = cls.TUPLE_SEP.join(value)
        else:
            cls.config[section][key] = value

    @classmethod
    def config_iterater(cls, config):
        for section, items in config.items():
            yield (cls.SECTION_NAME_FLG, (section, items.pop(cls.SECTION_EXPLAIN_NAME,"")))
            for name, data in items.items():
                yield (name, data)


if __name__ == "__main__":
    print(Setting.read("PATH", "root"))