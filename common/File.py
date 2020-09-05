import os

class File:

    def __init__(self, path_string):
        """
        1. create file path list and store instance variavle.
        2. store file name from last index of path list.
        3. store file size via os librally with file path.
        :param path: list of path except separators. ex: [dir, dir, file]
                     list object to express the path of this file.
                     a path is used different separators among some os.
                     so path is list except separators.
        """
        self._path = self.create_path(path_string)
        self._name = self._path[-1]

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

    def get_root_path(self, path_string):
        """
        judge os  from root path of file path.
        when separate the path as list, first index consider root path.
        if root path is ""(linux and mac is empty string, because separate by a os separator.),
        root path is "/".
        else root path is first index("C:", "D:"etc..).
        :param path_string:
        :return: root_path: first index of path list.
        """

    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_size(self):
        pass

    def get_path(self):
        pass

    def set_path(self, path):
        pass

    name = property(get_name, set_name, None, "file name. set_name is able to over write file name.")
    size = property(get_size, None, None, "file size. size is read only")
    path = property(get_path, set_path, None, "file path. set_path is able to move file to set path.")