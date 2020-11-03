import os
import sys
sys.path.append(os.path.abspath("../.."))

from common.setting.Setting import Setting

class ClientSetting(Setting):
    # ROOT_PATH_TAPLE = ("D:\\", "create", "python", "fileServer", "client")
    # CREATE_FILE_MODE = 0o777
    pass

if __name__ == "__main__":
    print(ClientSetting.read("PATH", "root", is_tuple=True))