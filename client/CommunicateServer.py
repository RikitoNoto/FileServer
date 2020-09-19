import socket
import random
from threading import Timer

import os
import sys
sys.path.append(os.path.abspath(".."))

from common.CONST import COMMAND
from common.CONST import PACKET

class CommunicateServer:
    MIN_PORT = 5500
    SOCKET_COUNT = 4
    RETRY_TIME = 1
    TIME_OUT = 10
    ERROR_CORD = None

    def __init__(self, ip):
        self.ip = ip

    def communicate(self, command, data, timecount=0):
        response = self.ERROR_CORD
        message = self.create_send_message(command, data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            port_list = [self.MIN_PORT + i for i in range(self.SOCKET_COUNT)]
            while port_list:
                while True:
                    port = self.MIN_PORT + random.randint(0, self.SOCKET_COUNT)
                    if port in port_list:
                        port_list.remove(port)
                        break
                try:
                    sock.connect(self.ip, port)
                    sock.send(message)
                    response = sock.recv(1024)
                    break
                except socket.error:
                    if not port_list:
                        Timer(self.RETRY_TIME, self.communicate, args=(command, data), kwargs=((timecount + self.RETRY_TIME),))
        return response

    def get_directory(self, path_list):
        path = self.create_abs_path(path_list)
        self.communicate(COMMAND.GET_DIR, path)

    def create_abs_path(self, path_list):
        path = PACKET.join(path_list)
        return path

    def create_send_message(self, command, data):
        message = "{}{}{}".format(command, PACKET.COMMAND_SEP, data)
        return message.encode()