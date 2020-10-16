from .FileSystem import FileSystem

class File(FileSystem):

    def get_content(self):
        with open(self.abs_path, mode="rb") as file:
           content = file.read()
        return content

    def set_content(self, content):
        with open(self.abs_path, mode="wb") as file:
            file.write(content)

    content = property(get_content, set_content, None, "file size. size is read only")