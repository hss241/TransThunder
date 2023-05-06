import requests
import json
from googletrans import Translator
import re
import colorama
import win_unicode_console
from time import sleep

class Message():
    def __init__(self, lang):
        self.lang = lang
        self.battle = False
        self.lastId = 0
        win_unicode_console.enable()
        colorama.init(autoreset=True)

    def checker(self):   #翻訳するメッセージの選択
        res = []
        lastIdList = ['0', str(self.lastId)]
        for parameter in lastIdList:
            try:
                res = json.loads(requests.get('http://localhost:8111/gamechat?lastId=' + parameter).text)
            except: #ゲームが起動していない場合
                self.lastId = 0
            if (len(res) == 0): #新規メッセージがない場合
                if (parameter == '0' and self.battle is True):  #試合していないかつ既に戦闘後の場合
                    self.battle = False
                sleep(1)
                return res

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
            self.battle = True

        reset = colorama.Back.RESET
        if (res['enemy'] == True):
            res['team'] = colorama.Back.RED + ';' + reset + ' '
        else:
            res['team'] = colorama.Back.CYAN + ':' + reset + ' '
        print(res['team'] + res['sender'] + " [" + res['mode'] + "]", end="")

        res['trans'] = Translator().translate(res['msg'], dest = self.lang).text

        print ("\r\n" + res['msg'] + "\r\n" + res['trans'] + "\r\n")
        
        return json.dumps(res)
