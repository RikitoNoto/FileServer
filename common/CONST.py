class COMMAND:
    GET_DIR = "getDirectory"


class PACKET:
    PATH_SEP = "/"
    COMMAND_SEP = " "
    DIRECTORY_SEP = " "
    DIRECTORY_SIGN = "D"
    FILE_SIGN = "F"
    HEADER_LENGTH = 1

class CONNECTION:
    SERVER_IP = "192.168.56.1"
    MIN_PORT = 5500
    SOCKET_COUNT = 4
    RETRY_TIME = 1
    TIME_OUT = 10
    ERROR_CORD = None