class COMMAND:
    GET_DIR = "getDirectory"


class PACKET:
    PATH_SEP = "/"
    COMMAND_SEP = " "
    DIRECTORY_SEP = " "

class CONNECTION:
    SERVER_IP = "192.168.11.6"
    MIN_PORT = 5500
    SOCKET_COUNT = 4
    RETRY_TIME = 1
    TIME_OUT = 10
    ERROR_CORD = None