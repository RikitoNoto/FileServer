import re
import pickle
from io import BytesIO
from .CONST import PACKET


class PacketMessage:

    def __init__(self, message:str = None, header:str = None, binary:bytes = None):
        if message and binary:
            raise ValueError("can not set message and binary togather.")
        elif not message and not binary:
            raise ValueError("set which one of message or binary.")
        elif message:
            self.__message:str = message
            self.__header:str = header
        elif binary:
            self.header, self.message = self.decode(binary)



    @staticmethod
    def decode(binary:bytes=b"") -> tuple:
        message_object:PacketMessage = pickle.load(binary)
        header = message_object.header
        message = message_object.message
        return header, message

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