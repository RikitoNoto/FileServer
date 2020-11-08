from configparser import SectionProxy
from configparser import ConfigParser
import os
import sys
sys.path.append(os.path.abspath("../.."))

from common.setting.Setting import Setting

class ServerSetting(Setting):

    @classmethod
    def config_dict(cls):
        try:
            cls.config
        except AttributeError:
            cls.config_load()
        return cls.config_iterater(cls.config)




if __name__ == "__main__":
    ServerSetting.CONFIG_FILE_PATH = "./setting.ini"#for debug
    ServerSetting.setting_dict()
