import tkinter as tk
import os
import sys
sys.path.append(os.path.abspath(".."))

from common.UI.IconButton import IconButton

class OptionButton(IconButton):
    POWER_DOWN_IMAGE = "../../resources/images/setting_gear.png"
    POWER_UP_IMAGE = "../../resources/images/setting_gear.png"
    HEIGHT_IMAGE_BIAS = 0
    WIDTH_IMAGE_BIAS = 0

    def __init__(self, master=None, **kwargs):
        IconButton.__init__(self, master=master, up_image=self.POWER_UP_IMAGE, down_image=self.POWER_DOWN_IMAGE, scale=1)
        self.configure(activebackground=None)


    def command_method(self):
        self.master.option_button_clicked()