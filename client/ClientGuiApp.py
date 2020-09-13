import tkinter

class ClientGuiApp:
    APP_NAME = "FileServer"
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 500
    def __init__(self):
        root = tkinter.Tk()
        root.title(self.APP_NAME)
        root.geometry("{}x{}".format(self.WINDOW_HEIGHT, self.WINDOW_WIDTH))
        self.set_parts(root)
        root.mainloop()

    def set_parts(self, root):
        pass