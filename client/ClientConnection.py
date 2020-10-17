import socket
import random
from threading import Timer

import os
import sys
sys.path.append(os.path.abspath(".."))

from common.FileSystem import FileSystem
from common.CommandPacket import CommandPacket
from common.PacketMessage import PacketMessage
from common.CONST import COMMAND
from common.CONST import PACKET
from common.CONST import CONNECTION

class ClientConnection(FileSystem):

    def communicate(self, command="", header="", data="", timecount=0):
        send_packet = CommandPacket(command=command, data=data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            port_list = [CONNECTION.MIN_PORT + i for i in range(CONNECTION.SOCKET_COUNT)]
            while port_list:
                if len(port_list) > 0:
                    index = random.randint(0, len(port_list) - 1)
                    port = port_list[index]
                    try:
                        sock.connect((CONNECTION.SERVER_IP, port))
                        print(send_packet.message)
                        sock.send(send_packet.value)
                        binary_packet = sock.recv(PACKET.PACKET_SIZE)
                        packet:PacketMessage = PacketMessage.decode(binary=binary_packet)
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
        return packet