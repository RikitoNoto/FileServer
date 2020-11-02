import tkinter as tk
import os
import sys
sys.path.append(os.path.abspath(".."))

from common.UI.SettingTextBox import SettingTextBox

class OptionFrame(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.create_widgets()

    def create_widgets(self):
        SettingTextBox(self, text="IP address:", bg="white")