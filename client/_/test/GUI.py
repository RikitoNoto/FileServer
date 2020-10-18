import tkinter as tk
import SevenSegment

root = tk.Tk()
root.title("FileNameChanger")
root.geometry("500x500")

# frame = tk.Frame(root, background = "#FF0000", width = 200, height = 200)
# label = tk.Label(frame, text = "test")
# text_box = tk.Entry(frame)
# list_box = tk.Listbox(frame)
#
# label.pack()
# text_box.pack()
# list_box.pack()
#
# frame.place(x = 300, y = 100)

a = SevenSegment.SevenSegment(root)
a.display().pack()

root.mainloop()