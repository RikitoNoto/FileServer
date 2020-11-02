import tkinter as tk
from ServerConnection import ServerConnection
from GUI.ServerApp import ServerApp

class ServerSystem(tk.Tk):

    def __init__(self):
        self.root = tk.Tk()
        ServerApp(self, self.root)
        self.root.mainloop()

    def server_start(self):
        self.server = ServerConnection()
        self.server.open_port()

    def server_close(self):
        self.server.close_port()

if __name__ == "__main__":
    ServerSystem()