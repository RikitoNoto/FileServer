import os
from FileSystem import FileSystem

class File(FileSystem):
    pass

if __name__ == "__main__":
    file = File(["_", "test"])
    print(file)
    print(file.path)
    print(file.size)