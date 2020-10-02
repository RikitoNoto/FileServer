from .Button import Button

import os
import sys

sys.path.append("../..")
from common.CONST import PACKET
from common.CONST import COMMAND

class ClientDirectory(Button):

    def click(self):
        children_dict = self.get_children(self.path_list)
        self.master.directory_clicked(self.path_list, children_dict)

    def get_children(self, path_list):
        print(path_list)
        path = self.create_packet_path(path_list)
        response = self.communicate(COMMAND.GET_DIR, path)
        file_dir_dict = self.create_file_dir_dict(response.decode(), path_list)
        return file_dir_dict

    def create_file_dir_dict(self, dir_string, dir_path_list):
        dir_list = dir_string.split(PACKET.DIRECTORY_SEP)
        file_dir_dict = {}
        for name in dir_list:
            kind = name[:PACKET.HEADER_LENGTH]
            name = name[PACKET.HEADER_LENGTH:]
            path_list = dir_path_list.copy()
            path_list.append(name)
            if kind == PACKET.DIRECTORY_SIGN:
                file_dir_dict[name] = self.master.DIRECTORY_FLG
            elif kind == PACKET.FILE_SIGN:
                file_dir_dict[name] = self.master.FILE_FLG
        return file_dir_dict
