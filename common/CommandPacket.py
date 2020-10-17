from .PacketMessage import PacketMessage
import re
import os
import sys
sys.path.append(os.path.abspath(".."))

from common.CONST import PACKET

class CommandPacket(PacketMessage):
    MESSAGE_TYPE = "COMMAND"

    def __init__(self, command=None, data=None, header=None):
        if command and data:
            self.__command = command
            self.__data = data
            message = self.create_message(command, data)
            PacketMessage.__init__(self, message=message, header=header)
        else:
            PacketMessage.__init__(self)
            self.__command, self.__data = self.separate_message(self.message)

    @staticmethod
    def create_message(command:str=None, data:str=None)->str:
        if command or data:
            message = "{}{}{}".format(command, PACKET.COMMAND_SEP, data)
            return message

    @staticmethod
    def separate_message(message:str)->tuple:
        retext = re.compile("(.*?){}(.*)".format(PACKET.COMMAND_SEP))
        match = retext.match(message)
        command = match.group(1)
        data = match.group(2)
        return command, data

    def get_command(self):
        return self.__command

    def set_command(self, command):
        self.__command = command

    def del_command(self):
        self.__command = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def del_data(self):
        self.__data = None

    def get_message(self):
        return self.create_message(self.__command, self.__data)

    def set_message(self, message):
        self.__command, self.__data = self.separate_message(message)

    def del_message(self):
        self.__command = None
        self.__data = None

    command = property(get_command, set_command, del_command, "action to do in server")
    data = property(get_data, set_data, del_data, "argument of command")