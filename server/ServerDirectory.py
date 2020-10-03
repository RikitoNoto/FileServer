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
        for i, directory in enumerate(directory_list):
            path = os.path.join(self.abs_path, directory)
            print(directory)
            if os.path.isdir(path):
               directory_list[i] = PACKET.DIRECTORY_SIGN + directory
            elif os.path.isfile(path):
                directory_list[i] = PACKET.FILE_SIGN + directory
        return PACKET.DIRECTORY_SEP.join(directory_list)