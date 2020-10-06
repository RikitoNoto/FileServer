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

    def communicate(self, command="", header="", data="", timecount=0):
        response = CONNECTION.ERROR_CORD
        message = self.create_send_message(command, header, data)
        print("connection start")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            port_list = [CONNECTION.MIN_PORT + i for i in range(CONNECTION.SOCKET_COUNT)]
            print("port list : {}".format(port_list))
            while port_list:
                if len(port_list) > 0:
                    index = random.randint(0, len(port_list) - 1)
                    port = port_list[index]
                    try:
                        sock.connect((CONNECTION.SERVER_IP, port))
                        print(message)
                        sock.send(message)
                        response = sock.recv(PACKET.PACKET_SIZE)
                        break
                    except socket.error:
                        if timecount < CONNECTION.TIME_OUT:
                            Timer(CONNECTION.RETRY_TIME, self.communicate, args=(), kwargs={"command": command, "header": header, "data": data,"timecount":(timecount + CONNECTION.RETRY_TIME)})
                        else:
                            print("error connection time out.")
                else:
                    print("connection is full")
                    break
        print("connection finish")
        return response

    def create_packet_path(self, path_list):
        path = PACKET.COMMAND_SEP.join(path_list)
        return path

    def create_send_message(self, command="", header="", data=""):
        message = "{}{}{}{}{}".format(command, PACKET.COMMAND_SEP, header, PACKET.HEADER_SEP, data)
        return message.encode()