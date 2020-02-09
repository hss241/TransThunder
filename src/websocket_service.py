from websocket_server import WebsocketServer

class Websocket():
    def __init__(self, sock_port, host):
        self.server = None
        self.port = sock_port
        self.host = host

    def send_message(self, res):
        self.server.send_message_to_all(res)   #クライアントにメッセージを送信

    def setEndPoint(self):
        self.server = WebsocketServer(int(self.port), host=self.host)  #クライアント側とのリアルタイム通信に必要

    def main(self):
        self.setEndPoint()
        self.server.run_forever()    #クライアントからの接続を待つ
        
