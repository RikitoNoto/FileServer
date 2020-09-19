from Button import Button

class Directory(Button):

    def click(self):
        self.master.directory_clicked()

    @classmethod
    def get_children(self, pathList):
        """パスリストを受け取り子ファイルを返す"""