
from FileFactory import FileFactory
import os
import sys
sys.path.append(os.path.abspath(".."))

from common.CONST import COMMAND
from common.CONST import PACKET

class ServerAction:
    COMMAND_METHOD = {COMMAND.GET_DIR: "get_directory"}

    def do_action(self, command, data):
        action = eval("self.{}".format(self.COMMAND_METHOD[command]))
        return action(data)

    def get_directory(self, data):
        path_list = self.__create_path_list(data)
        directory = FileFactory.file_factory(path_list)
        return directory.get_children()

    def get_file(self, data):
        print(data)

    def __create_path_list(self, path):
        path_list = path.split(PACKET.COMMAND_SEP)
        return path_list



if __name__ == "__main__":
    action = ServerAction()
    action.do_action(COMMAND.GET_DIR, "path")