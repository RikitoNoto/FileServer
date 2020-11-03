import os
import sys
from setting.ServerSetting import ServerSetting

sys.path.append(os.path.abspath(".."))

from common.Directory import Directory
from common.CONST import PACKET

class ServerDirectory(Directory):

    def get_abs_directory_path_list(self):
        return ServerSetting.read("PATH", "root", is_tuple=True)

    def get_children(self)->list:
        children_list = os.listdir(self.abs_path)
        return children_list

    children = property(get_children, None, None, "list of the children file or directory of this directory.")