import tkinter as tk
from GUI.ClientApp import ClientApp

class ClientSystem:

    #TODO GUIアプリ起動
    #TODO ボタン配置
    #TODO ボタンクリックイベント

    def __init__(self):
        root = tk.Tk()
        app = ClientApp(master=root)
        root.mainloop()

if __name__ == "__main__":
    ClientSystem()