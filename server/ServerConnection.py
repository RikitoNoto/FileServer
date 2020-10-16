import socket
import re
from multiprocessing import Process
from ServerAction import ServerAction

import os
import sys
sys.path.append(os.path.abspath(".."))

from common.CommandPacket import CommandPacket
from common.PacketMessage import PacketMessage
from common.CONST import CONNECTION
from common.CONST import PACKET

class ServerConnection(ServerAction):

    def open_port(self):
        process_list = []
        for i in range(CONNECTION.SOCKET_COUNT):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                socket_process = Process(target=self.create_socket, args=(sock, CONNECTION.MIN_PORT + i))
                process_list.append(socket_process)
                socket_process.start()

    def create_socket(self, sock, port):
        sock.bind((CONNECTION.SERVER_IP, port))
        sock.listen(1)

        while True:
            connection, address = sock.accept()

            with connection:
                while True:
                    message = connection.recv(PACKET.PACKET_SIZE)
                    if not message:
                        print("No message, so disconnect.")
                        break
                    command_packet = CommandPacket(binary=message)

                    packet:PacketMessage = self.do_action(command_packet)
                    connection.send(packet.value)

    def add_header(self, message):
        message = PACKET.HEADER_SEP + message
        return message

    def __decode_message(self, message):
        message = message.decode()
        regrep = re.compile("(.*?){}(.*?){}(.*)".format(PACKET.COMMAND_SEP, PACKET.HEADER_SEP))
        match = regrep.match(message)
        command = match.group(1)
        header = match.group(2)
        data = match.group(3)
        return (command, header, data)

if __name__ == "__main__":
    pass