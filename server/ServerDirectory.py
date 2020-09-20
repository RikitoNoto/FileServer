import os
import sys
sys.path.append(os.path.abspath(".."))

from common.FileSystem import FileSystem

class ServerDirectory(FileSystem):

    def get_children(self):
        children = os.listdir(self.__abs_path)
        return children