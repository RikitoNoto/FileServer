import re
import pickle
from io import BytesIO
from .CONST import PACKET


class PacketMessage:
    MESSAGE_TYPE = "DEFAULT"

    def __init__(self, message:str = None, header:str = None):
        if not message :
            raise ValueError("set message or header.")
        elif message:
            self.__message:str = message
            self.__header:str = header

    @staticmethod
    def decode(binary:bytes=b""):
        byte_file = BytesIO(binary)
        message_object:PacketMessage = pickle.load(byte_file)
        return message_object

    def get_message(self):
        return self.__message

    def set_message(self, content):
        self.__message = content

    def del_message(self):
        self.__message = None

    def get_header(self):
        return self.__header

    def set_header(self, content):
        self.__header = content

    def del_header(self):
        self.__header = None

    def get_value(self):
        file = BytesIO()
        pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)
        return file.getvalue()

    message = property(get_message, set_message, del_message, "content to communicate server or client.")
    header = property(get_header, set_header, del_header, "information to express this packet.")
    value = property(get_value, None, None, "binary text to send network.")