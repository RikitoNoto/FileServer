
from ServerFile import ServerFile
from ServerDirectory import ServerDirectory

import os
import sys
sys.path.append(os.path.abspath(".."))

from common.FileSystem import FileSystem

class ServerFileFactory:
    @staticmethod
    def file_factory(pathList):
        print(pathList)
        abs_path = os.path.join(FileSystem.SERVER_DIRECTORY_PATH, *pathList)
        if os.path.isfile(abs_path):
            return ServerFile(pathList)
        elif os.path.isdir(abs_path):
            return ServerDirectory(pathList)
        elif os.path.islink(abs_path):
            return None