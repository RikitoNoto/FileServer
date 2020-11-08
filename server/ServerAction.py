
from ServerFileFactory import ServerFileFactory
import os
import sys
sys.path.append(os.path.abspath(".."))

from common.PacketMessage import PacketMessage
from common.CommandPacket import CommandPacket
from common.CONST import COMMAND
from common.CONST import PACKET

class ServerAction:
    COMMAND_METHOD = {COMMAND.GET_DIR: "get_directory", COMMAND.GET_FILE: "get_file"}

    def do_action(self, packet:CommandPacket)-> PacketMessage:
        action = eval("self.{}".format(self.COMMAND_METHOD[packet.command]))
        return action(packet.data)

    def get_directory(self, data)->PacketMessage:
        path_list = PacketMessage.create_path_list(data)
        directory = ServerFileFactory.file_factory(path_list)
        childrenString:str = self.__convert_string_from_directory_list(directory)
        return PacketMessage(message=childrenString)

    def get_file(self, data)->PacketMessage:
        path_list = PacketMessage.create_path_list(data)
        file = ServerFileFactory.file_factory(path_list)
        return PacketMessage(message=file.content)

    def __convert_string_from_directory_list(self, directory):
        children_list = directory.children
        for i, name in enumerate(children_list):
            path = os.path.join(directory.abs_path, name)
            if os.path.isdir(path):
               children_list[i] = PACKET.DIRECTORY_SIGN + name
            elif os.path.isfile(path):
                children_list[i] = PACKET.FILE_SIGN + name
        return PACKET.DIRECTORY_SEP.join(children_list)



if __name__ == "__main__":
    action = ServerAction()
    action.do_action(COMMAND.GET_DIR, "path")