import tkinter as tk
import os
import sys
sys.path.append(os.path.abspath(".."))
from server.setting.ServerSetting import ServerSetting

sys.path.append(os.path.abspath("../.."))
from common.UI.SettingLable import SettingLable
from common.UI.SettingTextBox import SettingTextBox

class OptionFrame(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.create_options(ServerSetting.common_config_dict())
        self.create_options(ServerSetting.config_dict())

    def create_options(self, iterable_item):
        for name, data in iterable_item:
            if name == ServerSetting.SECTION_NAME_FLG:
                if data[0] == "DEFAULT":
                    continue
                SettingLable(self, text=data[0], explain=data[1], bg="white")
            elif name == ServerSetting.SECTION_EXPLAIN_NAME:
                pass
            else:
                SettingTextBox(self, text=name, place_holder=data, bg="white")