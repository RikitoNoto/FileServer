import configparser

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
    CONFIG_FILE_PATH = "setting/setting.ini"
    TUPLE_SEP = ","

    @classmethod
    def config_load(cls):
        cls.config:configparser.ConfigParser = configparser.ConfigParser()
        cls.config.read(cls.CONFIG_FILE_PATH)

    @classmethod
    def config_reset(cls):
        cls.config_load()

    @classmethod
    def config_save(cls):
        with open(cls.CONFIG_FILE_PATH, mode="w") as config_file:
            cls.config.write(config_file)

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

if __name__ == "__main__":
    print(Setting.read("PATH", "root"))