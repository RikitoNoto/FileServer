import tkinter as tk
from abc import ABC
from abc import abstractmethod

class SettingFrame(tk.Frame, ABC):

    def __init__(self, master=None, **kwargs):
        text = kwargs.pop("text", "")
        super().__init__(master=master, **kwargs)
        self.pack()
        self.__create_label(text)

    def __create_label(self, text):
        self.__lable = tk.Label(self, text=text)
        self.__lable.pack(side=tk.LEFT)