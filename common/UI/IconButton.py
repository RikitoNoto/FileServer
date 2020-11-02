import tkinter as tk

class IconButton(tk.Button):
    HEIGHT_IMAGE_BIAS = 35
    WIDTH_IMAGE_BIAS = 40
    UP_STATE = 1
    DOWN_STATE = 0

    def __init__(self, master=None, up_image="", down_image="", scale=1, **kwargs):
        super().__init__(master, kwargs)
        self.master = master
        self.up_image = tk.PhotoImage(file=up_image).subsample(scale)
        self.down_image = tk.PhotoImage(file=down_image).subsample(scale)

        self.configure(
            image=self.down_image,#image object need to be global variant.
            background=self.master["background"],
            activebackground=self.master["background"],
            border=0,
            command=self.reverse_image,
            height =self.up_image.height() - self.HEIGHT_IMAGE_BIAS,
            width =self.up_image.width() - self.WIDTH_IMAGE_BIAS
        )
        self.__state = self.DOWN_STATE

    def reverse_image(self):
        if self.state == self.UP_STATE:
            self.command_method(self.DOWN_STATE)
            self.state = self.DOWN_STATE
        else:
            self.command_method(self.UP_STATE)
            self.state = self.UP_STATE

    def command_method(self, state):
        pass

    def get_state(self):
        return self.__state

    def set_state(self, state):
        if state == self.UP_STATE:
            self.configure(image=self.up_image)
            self.__state = self.UP_STATE
        elif state == self.DOWN_STATE:
            self.configure(image=self.down_image)
            self.__state = self.DOWN_STATE



    state = property(get_state, set_state, None, "state of this button. return the value is const of this class.")