import tkinter as tk
from .SettingFrame import SettingFrame

class SettingLable(SettingFrame):

    def __init__(self, master=None, **kwargs):
        self.__explain = kwargs.pop("explain", "")
        kwargs.update({"side":tk.TOP, "anchor":tk.W, "text":"[" + kwargs["text"] + "]"})
        super().__init__(master=master, **kwargs)
        self.__create_explain()

    def __create_explain(self):
        self.__explain_label = tk.Label(self, text=self.__explain)
        self.__explain_label.pack(side=tk.TOP, anchor=tk.W)