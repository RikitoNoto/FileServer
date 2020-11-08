import tkinter as tk
from .SettingFrame import SettingFrame

class SettingTextBox(SettingFrame):

    def __init__(self, master=None, **kwargs):
        self.__place_holder = kwargs.pop("place_holder", "")
        super().__init__(master=master, **kwargs)
        self.__create_entry()

    def __create_entry(self):
        self.__entry = tk.Entry(self, width=int(self.master["width"]/10))
        self.__entry.pack(side=tk.RIGHT)
        self.__entry.insert(tk.END, self.__place_holder)