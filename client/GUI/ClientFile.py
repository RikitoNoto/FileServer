import os
import sys
import tkinter.messagebox as tkmsg
from .Button import Button

sys.path.append(os.path.abspath(".."))

from setting.ClientSetting import ClientSetting

sys.path.append(os.path.abspath("../.."))

from common.File import File
from common.CONST import COMMAND
from common.CONST import PACKET
from common.PacketMessage import PacketMessage

class ClientFile(File, Button):

    def get_abs_directory_path_list(self):
        return ClientSetting.ROOT_PATH_TAPLE

    def click(self, event):
        if tkmsg.askokcancel(title="Confirmation write", message="Do over write this file."):
            packet_path_list = PacketMessage.create_packet_path(self.path_list)
            packet:PacketMessage = self.communicate(command=COMMAND.GET_FILE, data=packet_path_list)
            self.master.file_clicked(self, packet.message)

if __name__ == "__main__":
    file = File(["_", "test"])
    print(file)
    print(file.path)
    print(file.size)