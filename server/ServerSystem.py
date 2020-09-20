from ServerConnection import ServerConnection

class ServerSystem:

    def __init__(self):
        server = ServerConnection()
        server.open_port()
    #TODO サーバーを開く
    #TODO パスを受信する機能
    #TODO パスがディレクトリなら構造を返す
    #TODO パスがファイルならファイルの内容を返す

if __name__ == "__main__":
    ServerSystem()