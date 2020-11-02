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
            port = CONNECTION.MIN_PORT
            try:
                sock.connect((CONNECTION.SERVER_IP, port))
                sock.send(send_packet.value)
                binary_packet:bytes = b""
                while not PacketMessage.is_response_end(binary_packet):
                    response = sock.recv(PACKET.PACKET_SIZE)
                    binary_packet += response
                packet:PacketMessage = PacketMessage.decode(binary=binary_packet)
            except socket.error:
                print("error {}".format(port))
                if timecount < CONNECTION.TIME_OUT:
                    Timer(CONNECTION.RETRY_TIME, self.communicate, args=(), kwargs={"command": command, "header": header, "data": data,"timecount":(timecount + CONNECTION.RETRY_TIME)})
                else:
                    print("error connection time out.")
        print("connection finish")
        return packet