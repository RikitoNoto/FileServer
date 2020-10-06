
from ServerFileFactory import ServerFileFactory
import os
import sys
sys.path.append(os.path.abspath(".."))

from common.CONST import COMMAND
from common.CONST import PACKET

class ServerAction:
    COMMAND_METHOD = {COMMAND.GET_DIR: "get_directory", COMMAND.GET_FILE: "get_file"}

    def do_action(self, command, header, data):
        action = eval("self.{}".format(self.COMMAND_METHOD[command]))
        return action(header, data)

    def get_directory(self, header, data):
        path_list = self.__create_path_list(data)
        directory = ServerFileFactory.file_factory(path_list)
        return directory.get_children()

    def get_file(self, header, data):
        path_list = self.__create_path_list(data)
        file = ServerFileFactory.file_factory(path_list)
        return file.content

    def __create_path_list(self, path):
        path_list = path.split(PACKET.COMMAND_SEP)
        return path_list



if __name__ == "__main__":
    action = ServerAction()
    action.do_action(COMMAND.GET_DIR, "path")