import tkinter as tk
import os
import sys
sys.path.append(os.path.abspath(".."))

from common.UI.IconButton import IconButton

class PowerButton(IconButton):
    POWER_DOWN_IMAGE = "../resources/images/power_button_down.png"
    POWER_UP_IMAGE = "../resources/images/power_button_up.png"

    def __init__(self, master=None, **kwargs):
        IconButton.__init__(self, master=master, up_image=self.POWER_UP_IMAGE, down_image=self.POWER_DOWN_IMAGE, scale=3)


    def command_method(self, state):
        self.master.power_button_clicked(state)