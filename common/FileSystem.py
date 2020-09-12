import os
from abc import ABC
from abc import abstractmethod

class FileSystem(ABC):
    SERVER_DIRECTORY_PATH = "/Users/ta4/python/FileServer"
    ROOT_PATH = "_"
    """
    
    """

    def __init__(self, path_list):
        """
        define the base process of file system.(common process of file and directory)
        file and directory need to be created under this file.
        so if operation system is Windows, the drive name have to be same this file's.
        1. create file path list and store instance variavle.
        2. store file name from last index of path list.
        3. store file size via os librally with file path.
        :param path_list: list of path except separators. ex: [dir, dir, file]
                          list object to express the path of this file.
                          a path is used different separators among some os.
                          so path is list except separators.
        """
        if path_list[0] != self.ROOT_PATH:
            path_list.insert(0, self.ROOT_PATH)
        self.__path_list = path_list
        self.__abs_path = self.__get_abs_path(self.path)
        self.__abs_dir = self.__get_abs_path(os.path.join(*self.__path_list[:-1]))
        self.__name = self.__path_list[-1]

    def __repr__(self):
        return self.name

    def create_path(self, path_string):
        """
        path of string convert path list object.
        first, judge the kind of os.
        next, path string store a path list with root path.
        :param path_string: string except file path.
        :return:
                path: list of path except separators. ex: [dir, dir, file]
                      list object to express the path of this file.
                      a path is used different separators among some os.
                      so path is list except separators.
        """

    def get_name(self):
        return self.__name

    def set_name(self, name=None, pathList=None):
        if pathList:
            path = self.__get_abs_path(os.path.join(*pathList))
            os.rename(self.__abs_path, path)
        elif name:
            os.rename(self.__abs_path, self.__get_abs_path(os.path.join(self.__abs_dir, name)))

    def get_size(self):
        return self.__get_dir_size(self.__abs_path)

    def get_path(self):
        return os.path.join(*self.__path_list)

    def set_path(self, path_list):
        pass

    def __get_abs_path(self, path):
        """
        return the actual abstract path of the file or the directory.
        users can not look the path, so this method is private method.
        this method is used to caculate file size.
        :return: the actual abstract path
        """
        abs_path = os.path.join(self.SERVER_DIRECTORY_PATH, path)
        return abs_path

    def __get_dir_size(self, abs_path):
        size = 0
        if os.path.isfile(abs_path):
            size = self.__get_file_size(abs_path)
        elif os.path.isdir(abs_path):
            for dir_content in os.scandir(abs_path):
                size += self.__get_dir_size(dir_content.path)
        return size


    def __get_file_size(self, path):
        abs_path = self.__get_abs_path(path)
        return os.path.getsize(abs_path)

    name = property(get_name, set_name, None, "file name. set_name is able to over write file name.")
    size = property(get_size, None, None, "file size. size is read only")
    path = property(get_path, set_path, None, "file path. set_path is able to move file to set path.")