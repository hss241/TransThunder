from config import Config
from translate import Translate
from websocket_service import Websocket
from time import sleep
from flask import Flask, render_template, request, jsonify
from jinja2 import FileSystemLoader
from flask_cors import CORS
import threading
import socket
import logging
import os
import platform
if platform.system() == "Windows":
    import winsound

logging.disable(logging.FATAL)
CORS(Flask(__name__))

class Main(Flask):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(__name__, *args, **kwargs)
        self.jinja_loader = FileSystemLoader(self.resource_path('./templates'))
        c = Config()
        self.params = c.iniReader()
        self.sock_port = self.params['websocket']
        self.host = self.params['host']

        @self.route('/', methods=['GET'])
        def index():
            return render_template('index.html', port=self.sock_port)

        @self.route('/', methods=['POST'])
        def dns():
            ip = socket.gethostbyname(request.form["hostname"])
            return jsonify({"ip":ip})

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    def websock(self):
        self.w = Websocket(self.sock_port, self.host)
        self.w.main()

    def flask(self):
        self.run(debug=False, host=self.host, port=self.params['flask'])

    def beep(self):
        try:
            winsound.Beep(880, 1000)    #windows
        except:
            os.system('play -n synth %s sin %s' % (1000, 880))  #mac, linux

    def trans(self):
        t = Translate(self.params['lang'])
        while (True):
            sleep(1)
            res = t.msgChecker()
            if (len(res) >= 1 and self.params['beep'] == 'True'):
                self.beep()
            if (len(res) == 0 or res[0] == 'receive'):
                continue
            res = t.msgViewer(res)
            if (self.params['browse'] == 'True'):
                self.w.send_message(res)

    def clearConsole(self):
        try:
            os.system('cls')    #windows
        except:
            import subprocess as sp
            try:
                tmp = sp.call('cls',Shell=True) #mac
            except:
                tmp = sp.call('clear',Shell=True)   #linux

    def main(self):
        if (self.params['browse'] == 'True'):
            t1 = threading.Thread(target=self.websock)
            t1.start()
            t2 = threading.Thread(target=self.flask)
            t2.start()
        self.clearConsole()
        t3 = threading.Thread(target=self.trans)
        t3.start()
        t3.join()

if __name__ == '__main__':
    m = Main()
    m.main()

