import tkinter as tk

from ClientDirectory import ClientDirectory
from ClientConnection import ClientConnection

import sys
import os
sys.path.append(os.path.abspath(".."))

from common.FileSystem import FileSystem


class ClientApp(tk.Frame, FileSystem):

    def __init__(self, master=None, path=FileSystem.ROOT_PATH):
        super().__init__(master)
        self.master = master
        self.configure(
            height = 500,
            width = 1000,
            bg="red"
        )
        self.pack()
        self.propagate(False)#子要素によってリサイズされるのを無効にする

        self.current_path = path
        self.create_widgets()

    def __create_button(self):
        pass

    def create_widgets(self):
        self.button = ClientDirectory(self)
        self.button.pack()

    def directory_clicked(self):
        self.button.destroy()

    def file_clicked(self):
        pass
