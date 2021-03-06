class COMMAND:
    GET_DIR = "getDirectory"
    GET_FILE = "getFile"

class SYSTEM:
    ROOT_PATH = "_"

class PACKET:
    PACKET_SIZE = 1024 * 1024 * 1024
    PATH_SEP = "/"
    COMMAND_SEP = " "
    DIRECTORY_SEP = "/"
    DIRECTORY_SIGN = "D"
    FILE_SIGN = "F"
    HEADER_LENGTH = 1
    ENCORDING = 'utf-8'
    END_OF_MESSAGE = b"\x00\x00\x00\x00\x00\x00"

class CONNECTION:
    SERVER_IP = "192.168.12.6"
    MIN_PORT = 5500
    SOCKET_COUNT = 4
    RETRY_TIME = 1
    TIME_OUT = 10
    ERROR_CORD = None