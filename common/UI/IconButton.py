import tkinter as tk

class IconButton(tk.Button):
    HEIGHT_IMAGE_BIAS = 35
    WIDTH_IMAGE_BIAS = 40

    def __init__(self, master=None, up_image="", down_image="", scale=1, **kwargs):
        super().__init__(master, kwargs)
        self.master = master
        self.up_image = tk.PhotoImage(file=up_image).subsample(scale)
        self.down_image = tk.PhotoImage(file=down_image).subsample(scale)
        print(self.up_image.height())

        self.configure(
            image=self.down_image,#image object need to be global variant.
            background=self.master["background"],
            activebackground=self.master["background"],
            border=0,
            command=self.reverse_image,
            height =self.up_image.height() - self.HEIGHT_IMAGE_BIAS,
            width =self.up_image.width() - self.WIDTH_IMAGE_BIAS
        )
        self.state = self.down_image

    def reverse_image(self):
        self.command_method()
        if self.state == self.up_image:
            self.configure(image=self.down_image)
            self.state = self.down_image
        else:
            self.configure(image=self.up_image)
            self.state = self.up_image

    def command_method(self):
        pass