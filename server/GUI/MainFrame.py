import tkinter as tk
from PowerButton import PowerButton
from OptionButton import OptionButton

class MainFrame(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.power_button:tk.Button = PowerButton(self)
        self.option_button:tk.Button = OptionButton(self)
        self.power_button.pack(side=tk.LEFT, anchor=tk.CENTER)
        self.option_button.pack(side=tk.RIGHT, anchor=tk.CENTER)

    def option_button_clicked(self):
        self.master.change_option_frame()