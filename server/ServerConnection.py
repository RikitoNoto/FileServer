import socket
import re
from multiprocessing import Process
from multiprocessing import Value
from threading import Thread
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
        self.server_state = Value("b", 1)
        self.__process:Process  = Process(target=self.create_socket, args=(CONNECTION.MIN_PORT, self.server_state), daemon=True)

        self.process.start()

    def close_port(self):
        self.server_state.value = 0
        for _ in range(CONNECTION.SOCKET_COUNT+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((CONNECTION.SERVER_IP, CONNECTION.MIN_PORT))
            sock.close()
        self.process.join()
        del self.process

    def create_socket(self, port, state:Value):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock :
            sock.bind((CONNECTION.SERVER_IP, port))
            sock.listen(CONNECTION.SOCKET_COUNT)
            while state.value:
                connection, address = sock.accept()
                with connection:
                    while True:
                        message = connection.recv(PACKET.PACKET_SIZE)
                        if not message:
                            print("No message, so disconnect.")
                            break
                        packetMessage:PacketMessage = PacketMessage.decode(message)

                        send_message:PacketMessage = self.message_handling(packetMessage)
                        connection.send(send_message.value)


    def message_handling(self, packet:PacketMessage) -> PacketMessage:
        if packet.MESSAGE_TYPE == CommandPacket.MESSAGE_TYPE:
            response = self.do_action(packet)

        return response

    def get_process(self)->Process:
        return self.__process

    def del_process(self):
        self.__process.close()

    process = property(get_process, None, del_process, "the process that is the file server.")

if __name__ == "__main__":
    pass