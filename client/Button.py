import tkinter as tk
from abc import ABC
from abc import abstractmethod

import os
import sys
sys.path.append(os.path.abspath(".."))

from common.FileSystem import FileSystem

class Button(FileSystem, tk.Button, ABC):

    def __init__(self, master=None, pathList=None, cnf={}, **kw):
        if not pathList:
            pathList = self.ROOT_PATH
        FileSystem.__init__(self, pathList)

        tk.Button.__init__(self, master, cnf, **kw)
        self.configure(
            text = self.name,
            height = 1,
            width = self.master["width"],
            font = ("", 14),
            bg = "gray",
            fg = "black",
            command = self.click
        )
        self.configure(**kw)

    @abstractmethod
    def click(self):
        pass