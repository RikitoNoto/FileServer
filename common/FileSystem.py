import os
from abc import abstractmethod

class FileSystem:
    SERVER_DIRECTORY_PATH = os.path.join("D:\\", "create", "python", "fileServer", "server")
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
        self.__abs_dir = self.create_abs_path(os.path.join(*self.__path_list[:-1], ""))
        #if in path list is only root path, an error will occur when "" is noting.
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
            path = self.create_abs_path(os.path.join(*pathList))
            os.rename(self.abs_path, path)
        elif name:
            os.rename(self.abs_path, self.create_abs_path(os.path.join(self.__abs_dir, name)))

    def get_size(self):
        return self.__get_dir_size(self.abs_path)

    def get_path(self):
        return os.path.join(*self.__path_list)

    def set_path(self, path_list):
        pass

    def get_path_list(self):
        return self.__path_list

    def get_abs_path(self):
        return self.create_abs_path(self.path)

    def create_abs_path(self, path):
        """
        return the actual abstract path of the file or the directory.
        users can not look the path, so this method is private method.
        this method is used to caculate file size.
        :return: the actual abstract path
        """
        abs_path = os.path.join(self.abs_directory_path, path)
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
        abs_path = self.create_abs_path(path)
        return os.path.getsize(abs_path)

    @abstractmethod
    def get_abs_directory_path(self):
        return os.path.join(*self.get_abs_directory_path_list())

    @abstractmethod
    def get_abs_directory_path_list(self):
        pass

    name = property(get_name, set_name, None, "file name. set_name is able to over write file name.")
    size = property(get_size, None, None, "file size. size is read only")
    path = property(get_path, set_path, None, "file path. set_path is able to move file to set path.")
    path_list = property(get_path_list, None, None, "file path list. this is not abs path.")
    abs_path = property(get_abs_path, None, None, "this is an abstract path of this file os directory.")
    abs_directory_path = property(get_abs_directory_path, None, None, "abstract path of the directory up this file or this directory.")