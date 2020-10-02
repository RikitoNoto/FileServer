import tkinter as tk
from .ClientDirectory import ClientDirectory
from .ClientFile import ClientFile

import os
import sys
sys.path.append(os.path.abspath("../.."))

from common.FileSystem import FileSystem

class FilePane(tk.Frame):
    FONT_SIZE = 9
    PANE_SIZE = 9/10
    DIRECTORY_FLG = "directory"
    FILE_FLG = "file"

    def __init__(self, master=None, directory_dict=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)

        self.configure(
            height = (self.master["height"]*self.PANE_SIZE),
            width = self.master["width"],
            bg="#e4e6e7"
        )
        self.configure(**kw)
        self.pack()
        self.propagate(False)
        self.directory_list = []

        self.create_widgets(directory_dict)

    def create_widgets(self, directory_dict, directory_path_list=[]):
        self.clear_directory()
        for name, kind in directory_dict.items():
            path_list = directory_path_list.copy()
            path_list.append(name)
            if kind == self.DIRECTORY_FLG:
                directory = ClientDirectory(self, path_list)
                self.directory_list.append(directory)
                directory.pack()
            elif kind == self.FILE_FLG:
                file = ClientFile(self, path_list)
                self.directory_list.append(file)
                file.pack()

    def clear_directory(self):
        for directory in self.directory_list:
            directory.destroy()
        self.directory_list = []

    def directory_clicked(self, path_list, children_dict):
        self.create_widgets(children_dict, directory_path_list=path_list)


    def file_clicked(self):
        pass