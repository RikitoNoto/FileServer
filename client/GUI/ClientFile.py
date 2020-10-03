import os
from .Button import Button

class ClientFile(Button):

    def click(self, event):
        self.master.file_clicked()

if __name__ == "__main__":
    file = File(["_", "test"])
    print(file)
    print(file.path)
    print(file.size)