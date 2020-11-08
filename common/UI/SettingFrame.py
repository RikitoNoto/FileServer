import tkinter as tk
from abc import ABC
from abc import abstractmethod

class SettingFrame(tk.Frame, ABC):

    def __init__(self, master=None, **kwargs):
        text = kwargs.pop("text", "")
        anchor = kwargs.pop("anchor", tk.CENTER)
        side = kwargs.pop("side", tk.LEFT)
        propagate = kwargs.pop("propagate", True)
        super().__init__(master=master, **kwargs)
        self.propagate(propagate)
        self.pack(fill=tk.X)
        self.__create_label(text, anchor, side)

    def __create_label(self, text, anchor=tk.CENTER, side=tk.LEFT):
        self.__title_lable = tk.Label(self, text=text)
        self.__title_lable.pack(anchor=anchor, side=side)