from config import Config
from message import Message
from websocket_service import Websocket
from time import sleep
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
        self.sock_port = self.params["websocket"]
        self.host = self.params["host"]

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
        self.run(debug=False, host=self.host, port=self.params["flask"])

    def beep(self):
        winsound.Beep(880, 1000)

    def trans(self):
        m = Message(self.params["lang"], self.params["accuracy"])
        while (True):
            sleep(1)
            res = m.checker()
            if (len(res) >= 1 and self.params["beep"] == "True"):
                th = threading.Thread(target=self.beep)
                th.start()
            if (len(res) == 0 or res[0] == "receive"):
                continue
            res = m.viewer(res)
            if (self.params["browse"] == "True"):
                self.ws.send_message(res)

    def main(self):
        if (self.params["browse"] == "True"):
            th1 = threading.Thread(target=self.websock)
            th1.start()
            th2 = threading.Thread(target=self.flask)
            th2.start()
        os.system("cls")
        th3 = threading.Thread(target=self.trans)
        th3.start()
        th3.join()

if __name__ == "__main__":
    m = Main()
    m.main()

