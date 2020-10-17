from .Button import Button

import os
import sys

sys.path.append(os.path.abspath(".."))
from setting.ClientSetting import ClientSetting

sys.path.append("../..")
from common.Directory import Directory
from common.CONST import PACKET
from common.CONST import COMMAND
from common.PacketMessage import PacketMessage

class ClientDirectory(Directory, Button):

    def click(self, event):
        children_dict = self.get_children(self.path_list)
        self.master.directory_clicked(self, children_dict)

    def get_abs_directory_path_list(self):
        return ClientSetting.ROOT_PATH_TAPLE

    def get_children(self, path_list):
        path = PacketMessage.create_packet_path(path_list)
        packet:PacketMessage = self.communicate(command=COMMAND.GET_DIR, data=path)
        file_dir_dict = self.create_file_dir_dict(packet.message, path_list)
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
