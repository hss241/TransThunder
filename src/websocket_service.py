from websocket_server import WebsocketServer

class Websocket():
    def __init__(self, sock_port):
        self.server = None
        self.port = sock_port

    def send_message(self, res):
        self.server.send_message_to_all(res)   #クライアントにメッセージを送信

    def setEndPoint(self):
        self.server = WebsocketServer(int(self.port), host="0.0.0.0")  #クライアント側とのリアルタイム通信に必要

    def main(self):
        self.setEndPoint()
        self.server.run_forever()    #クライアントからの接続を待つ
        
