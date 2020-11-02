import tkinter as tk
from .MainFrame import MainFrame
from .OptionFrame import OptionFrame
from .PowerButton import PowerButton

class ServerApp(tk.Frame):
    def __init__(self, system=None, master=None):
        super().__init__(master)
        self.system = system
        self.master = master
        self.configure(
            height = 500,
            width = 1000,
            bg="white"
        )
        self.pack()
        self.propagate(False)

        self.create_widgets()

    def create_widgets(self):
        self.change_main_frame()

    def change_option_frame(self):
        try:
            self.current_frame.pack_forget()
        except AttributeError:
            pass
        self.current_frame:tk.Frame = OptionFrame(self,
                                                  height=self["height"],
                                                  width=self["width"],
                                                  background="black")#self["background"])
        self.current_frame.pack()

    def change_main_frame(self):
        try:
            self.current_frame.pack_forget()
        except AttributeError:
            pass
        self.current_frame:tk.Frame = MainFrame(self,
                                                background=self["background"],
                                                height=self["height"],
                                                width=self["width"]/2)
        self.current_frame.pack()

    def power_button_event(self, state):
        if state == PowerButton.UP_STATE:
            self.system.server_start()
        else:
            self.system.server_close()


if __name__ == "__main__":
    root = tk.Tk()
    ServerApp(root)
    root.mainloop()