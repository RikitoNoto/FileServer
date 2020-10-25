import tkinter as tk

class OptionFrame(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.create_widgets()

    def create_widgets(self):
        pass