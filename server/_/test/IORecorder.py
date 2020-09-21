import json
import os

class IORecorder:
    PATH = ("var", "lib", "TMT")
    def __init__(self, file_name):
        self.ROOT_PATH = os.getcwd().split(os.sep)[0]
        self.ROOT_PATH = self.ROOT_PATH if self.ROOT_PATH else "/"
        self.path = os.path.join(self.ROOT_PATH, self.PATH, file_name)


    def write(self, data):
        file = open(self.path, "w")
        file.write(data)

    def read(self):
        return open(self.path, "r")
