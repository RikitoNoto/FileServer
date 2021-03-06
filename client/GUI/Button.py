import tkinter as tk
from abc import ABC
from abc import abstractmethod

import os
import sys
sys.path.append(os.path.abspath(".."))

from ClientConnection import ClientConnection

class Button(ClientConnection, tk.Label, ABC):
    BACK_GROUND_COLOR = "#FFFFFF"

    def __init__(self, master=None, path_list=None, cnf={}, **kw):
        if not path_list:
            path_list = [self.ROOT_PATH]
        ClientConnection.__init__(self, path_list)

        tk.Label.__init__(self, master, cnf, **kw)
        self.configure(
            text = self.name,
            height = 1,
            width = self.master["width"],
            font = ("", 9),
            bg = self.BACK_GROUND_COLOR,
            bd = 0,
            fg = "black",
        )
        self.configure(**kw)
        self.set_event()


    @abstractmethod
    def click(self, event):
        pass

    def set_event(self):
        self.bind("<Leave>", self.leave)
        self.bind("<Enter>", self.enter)
        self.bind("<Double-Button-1>", self.click)

    def enter(self, event):
        self.config(bg="#CCE8FF")

    def leave(self, event):
        self.config(bg=self.BACK_GROUND_COLOR)