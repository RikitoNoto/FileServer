import os

from client.File import File
from client.Directory import Directory
from .FileSystem import FileSystem

class FileFactory:
    @staticmethod
    def file_factory(pathList):
        abs_path = os.path.join(FileSystem.SERVER_DIRECTORY_PATH, *pathList)
        if os.path.isfile(abs_path):
            return File(pathList)
        elif os.path.isdir(abs_path):
            return Directory(pathList)
        elif os.path.islink(abs_path):
            return None