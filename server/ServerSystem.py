import tkinter as tk
from ServerConnection import ServerConnection

class ServerSystem:

    def __init__(self):
        pass

    def server_start(self):
        self.server = ServerConnection()
        self.server.open_port()

if __name__ == "__main__":
    ServerSystem()