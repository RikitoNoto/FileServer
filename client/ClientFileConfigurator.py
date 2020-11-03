import os

from setting.ClientSetting import ClientSetting

class ClientFileConfigurator:

    def create_directory(self, directory):
        if not os.path.isdir(directory.abs_path):
            os.makedirs(directory.abs_path, mode=ClientSetting.read("FILE", "create_mode"))

    def create_file(self, file):
        if not os.path.isfile(file.abs_path):
            open(file.abs_path, mode="w").close()