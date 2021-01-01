import requests
import json
from googletrans import Translator
from deepyl import DeepyL
import re
import os
import colorama
import win_unicode_console
from time import sleep

class Message():
    def __init__(self, lang, deepl):
        self.lang = lang
        self.battle = False
        self.lastId = 0
        os.system("title TransThunder")
        if (deepl == "True" and any(lang in item for item in ["ja","en","de","fr","es","pt","it","nl","pl","ru","zh"])):
            try:
                self.deepl = DeepyL(lang)
            except:
                pass
        win_unicode_console.enable()
        colorama.init(autoreset=True)

    def checker(self):   #翻訳するメッセージの選択
        res = []
        while (len(res) == 0):
            lastIdList = ['0', str(self.lastId)]
            for parameter in lastIdList:
                try:
                    res = json.loads(requests.get('http://localhost:8111/gamechat?lastId=' + parameter).text)
                except: #ゲームが起動していない場合
                    self.lastId = 0
            else:
                if (len(res) == 0): #新規メッセージがない場合
                    if (parameter == '0'):  #試合していない場合
                        if (self.battle is True):
                            self.deepl.close()
                            self.battle = False
                    res = []
                    sleep(1)
                    continue

            res = res[0]
            self.lastId = res['id']
            res['msg'] = res['msg'].replace('\t', '')
            if (len(res) == 0 or re.search('<color=#\w*>', res['msg']) or
                Translator().detect(res['msg']).lang == self.lang or res['sender'] == ''):
                res = []
        return res

    def viewer (self, res):
        if (self.battle is False):
            print ('------------------------------')
            res['bar'] = '------------------------------'
            self.deepl.get()

        reset = colorama.Back.RESET
        if (res['enemy'] == True):
            res['team'] = colorama.Back.RED + ';' + reset + ' '
        else:
            res['team'] = colorama.Back.CYAN + ':' + reset + ' '
        print(res['team'] + res['sender'] + " [" + res['mode'] + "]", end="")

        if hasattr(self, "deepl"):
            res['use'] = " <DeepL>"
            res['trans'] = self.deepl.io(res['msg'])
        if (res['msg'] == res['trans'] or res['trans'] == ""):   #deepl未対応言語だった場合
            res['use'] = " <Google>"
            res['trans'] = Translator().translate(res['msg'], dest = self.lang).text

        print (res['use'] + "\r\n" + res['msg'] + "\r\n" + res['trans'] + "\r\n")
        self.battle = True

        return json.dumps(res)