import tkinter as tk
from .FilePane import FilePane

import sys
import os
sys.path.append(os.path.abspath("../.."))
sys.path.append(os.path.abspath(".."))


from ClientConnection import ClientConnection
from common.FileSystem import FileSystem


class ClientApp(tk.Frame, FileSystem):

    def __init__(self, master=None, path=FileSystem.ROOT_PATH):
        super().__init__(master)
        self.master = master
        self.configure(
            height = 500,
            width = 1000,
            bg="white"
        )
        self.pack()
        self.propagate(False)

        self.current_path = path
        self.create_widgets()

    def create_widgets(self):
        self.create_file_pane()

    def create_file_pane(self):
        self.file_pane = FilePane(self, {"_": FilePane.DIRECTORY_FLG})