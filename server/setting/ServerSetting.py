import os
import sys
sys.path.append(os.path.abspath("../.."))

from common.setting.Setting import Setting

class ServerSetting(Setting):
    pass



if __name__ == "__main__":
    config =ServerSetting()
    print(config.read("PATH", "root", is_tuple=True))
