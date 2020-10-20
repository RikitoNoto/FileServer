import tkinter as tk

class ServerApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
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
        image = tk.PhotoImage(file="../../resources/images/power_button.png")
        button = tk.Button(self, command=self.test)#, image=image)
        button.pack()

    def test(self):
        print("aaaa")

if __name__ == "__main__":
    root = tk.Tk()
    ServerApp(root)
    root.mainloop()