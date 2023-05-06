from update import Update
from config import Config
from message import Message
from websocket_service import Websocket
from flask import Flask, render_template, request, jsonify
from jinja2 import FileSystemLoader
from flask_cors import CORS
import threading
import socket
import logging
import os
import winsound
from resource_path import Resource_path

logging.disable(logging.FATAL)
CORS(Flask(__name__))

class Main(Flask):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(__name__, *args, **kwargs)
        self.jinja_loader = FileSystemLoader(Resource_path("./templates"))
        c = Config()
        self.params = c.iniReader()
        self.browse_port = self.params["browse_port"]
        self.sock_port = int(self.browse_port) - 1

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.host = s.getsockname()[0]

        @self.route("/", methods=["GET"])
        def index():
            return render_template("index.html", port=self.sock_port)

        @self.route("/", methods=["POST"])
        def dns():
            ip = socket.gethostbyname(request.form["hostname"])
            return jsonify({"ip":ip})

    def websock(self):
        self.ws = Websocket(self.sock_port, self.host)
        self.ws.main()

    def flask(self):
        self.run(debug=False, host=self.host, port=self.browse_port)

    def beep(self):
        winsound.Beep(880, 1000)

    def trans(self):
        m = Message(self.params["lang"])
        while (True):
            res = m.checker()
            if (len(res) == 0):
                continue
            res = m.viewer(res)
            if (self.params["beep"] == "True"):
                th = threading.Thread(target=self.beep)
                th.start()
                self.ws.send_message(res)

    def main(self):
        Update().check()
        th1 = threading.Thread(target=self.websock)
        th1.start()
        th2 = threading.Thread(target=self.flask)
        th2.start()
        os.system("cls")
        print('Access your browser to check translation results.')
        print('http://' + self.host + ':' + self.browse_port)

        th3 = threading.Thread(target=self.trans)
        th3.start()
        th3.join()

if __name__ == "__main__":
    m = Main()
    m.main()