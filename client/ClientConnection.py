import socket
import random
from threading import Timer

import os
import sys
sys.path.append(os.path.abspath(".."))

from common.FileSystem import FileSystem
from common.CONST import COMMAND
from common.CONST import PACKET
from common.CONST import CONNECTION

class ClientConnection(FileSystem):


    def communicate(self, command, data, timecount=0):
        response = CONNECTION.ERROR_CORD
        message = self.create_send_message(command, data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            port_list = [CONNECTION.MIN_PORT + i for i in range(CONNECTION.SOCKET_COUNT)]
            while port_list:
                while True:
                    port = CONNECTION.MIN_PORT + random.randint(0, CONNECTION.SOCKET_COUNT)
                    if port in port_list:
                        port_list.remove(port)
                        break
                try:
                    sock.connect((CONNECTION.SERVER_IP, port))
                    sock.send(message)
                    response = sock.recv(1024)
                    print(response)
                    break
                except socket.error:
                    if timecount < CONNECTION.TIME_OUT:
                        Timer(CONNECTION.RETRY_TIME, self.communicate, args=(command, data), kwargs=((timecount + CONNECTION.RETRY_TIME),))
                    else:
                        print("error connection time out.")
        return response

    def create_packet_path(self, path_list):
        path = PACKET.COMMAND_SEP.join(path_list)
        return path

    def create_send_message(self, command, data):
        message = "{}{}{}".format(command, PACKET.COMMAND_SEP, data)
        return message.encode()