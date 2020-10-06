import os
import sys
from setting.ServerSetting import ServerSetting

sys.path.append(os.path.abspath(".."))

from common.Directory import Directory
from common.CONST import PACKET

class ServerDirectory(Directory):

    def get_abs_directory_path_list(self):
        return ServerSetting.ROOT_PATH_TAPLE

    def get_children(self):
        children_list = os.listdir(self.abs_path)
        children_string = self.__convert_string_from_directory_list(children_list)
        return children_string.encode()

    def __convert_string_from_directory_list(self, directory_list):
        for i, directory in enumerate(directory_list):
            path = os.path.join(self.abs_path, directory)
            if os.path.isdir(path):
               directory_list[i] = PACKET.DIRECTORY_SIGN + directory
            elif os.path.isfile(path):
                directory_list[i] = PACKET.FILE_SIGN + directory
        return PACKET.DIRECTORY_SEP.join(directory_list)