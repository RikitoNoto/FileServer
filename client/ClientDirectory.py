from Button import Button
from ClientConnection import ClientConnection

class ClientDirectory(Button, ClientConnection):

    def click(self):
        self.get_children(self.path_list)
        self.master.directory_clicked()
