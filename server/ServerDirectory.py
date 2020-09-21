import os
import sys
sys.path.append(os.path.abspath(".."))

from common.FileSystem import FileSystem
from common.CONST import PACKET

class ServerDirectory(FileSystem):

    def get_children(self):
        children_list = os.listdir(self.abs_path)
        return self.__convert_string_from_directory_list(children_list)

    def __convert_string_from_directory_list(self, directory_list):
        return PACKET.DIRECTORY_SEP.join(directory_list)