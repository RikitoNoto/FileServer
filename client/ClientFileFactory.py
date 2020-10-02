import GUI

import os
import sys
sys.path.append(os.path.abspath(".."))

from common.CONST import PACKET

class ClientFileFactory:
    @staticmethod
    def file_factory(kind, path_list):
        if kind == PACKET.DIRECTORY_SIGN:
            return GUI.ClientDirectory.ClientDirectory(path_list)
        elif kind == PACKET.FILE_SIGN:
            return GUI.ClientDirectory.ClientFile(path_list)
        else:
            return None