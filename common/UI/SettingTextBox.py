import tkinter as tk
from .SettingFrame import SettingFrame

class SettingTextBox(SettingFrame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.__create_entry()

    def __create_entry(self):
        self.__entry = tk.Entry(self)
        self.__entry.pack(side=tk.RIGHT)