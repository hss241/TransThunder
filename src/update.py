import os
import sys
import requests
import codecs
import json
import subprocess

class Update():
    def __init__(self):
        self.version = "v3.4.1"
        os.system("title TransThunder " + self.version)

        self.dlurl = "https://github.com/hss241/TransThunder/blob/master/TransThunder.exe?raw=true"
        self.gitapi = "https://api.github.com/repos/hss241/transthunder/releases/latest"
        srcname = "@TransThunder.exe"
        dstname = "TransThunder.exe"

        basepath = os.path.dirname(os.path.abspath(sys.argv[0]))    #こうやって取らないと一時フォルダの方を取ってきちゃう
        self.srcpath = os.path.join(basepath, srcname)
        self.dstpath = os.path.join(basepath, dstname)

    def postprocess(self):
        if (os.path.exists(self.dstpath)):
            os.remove(self.dstpath)
        os.rename(self.srcpath, self.dstpath)

    def download(self):
        dlfile = codecs.open(self.srcpath, "wb")
        dlfile.write(requests.get(self.dlurl, timeout=(3.0, 9.0)).content)
        dlfile.close()

    def switch(self):
        try:
            self.download()
        except:
            pass
        else:
            subprocess.Popen(['start', self.srcpath], shell=True)
            sys.exit()

    def check(self):
        try:
            gitjson = requests.get(self.gitapi, timeout=(3.0, 9.0)).json()
        except Timeout:
            pass
        else:
            if (gitjson["tag_name"] != self.version):
                self.switch()
            elif (os.path.exists(self.srcpath)):
                self.postprocess()