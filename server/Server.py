import socket
from multiprocessing import Process

socket_count = 4
ip = "192.168.11.13"
min_port = 5500

def create_socket(s, port):
    s.bind((ip, port))
    s.listen(1)

    while True:
        connection, address = s.accept()

        with connection:
            while True:
                path = connection.recv(1024)

                if not path:
                    break

                print("メッセージを受信　ポート：{}, アドレス：{}".format(port, address))
                connection.send(b"send meaage")
                open()

if __name__ == "__main__":

    process_list = []
    for i in range(socket_count):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            socket_process = Process(target=create_socket, args=(sock, min_port+i))
            process_list.append(socket_process)
            socket_process.start()

    for p in process_list:
        p.join()