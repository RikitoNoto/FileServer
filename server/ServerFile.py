import os
import sys

from setting.ServerSetting import ServerSetting

sys.path.append(os.path.abspath(".."))

from common.File import File


class ServerFile(File):

    def get_abs_directory_path_list(self):
        return ServerSetting.read("PATH", "root", is_tuple=True)

