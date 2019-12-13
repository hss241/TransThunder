import requests
import json
from googletrans import Translator
import re
import os
import colorama
import win_unicode_console

class Translate():
    def __init__(self, lang):
        self.lang = lang
        self.battle = False
        self.lastId = 0
        win_unicode_console.enable()
        colorama.init(autoreset=True)

    def msgChecker(self):   #翻訳するメッセージの選択
        res = []
        lastIdList = ['0', str(self.lastId)]
        for parameter in lastIdList:
            try:
                res = json.loads(requests.get('http://localhost:8111/gamechat?lastId=' + parameter).text)
            except: #ゲームが起動していない場合
                self.lastId = 0
                return res
            if (len(res) == 0): #新規メッセージがない場合
                if (parameter == '0'):  #試合していない場合
                    self.battle = False
                return res

        self.lastId = res[0]['id']
        if (len(res) == 0 or re.search('<color=#\w*>', res[0]['msg']) or
            Translator().detect(res[0]['msg']).lang == self.lang or res[0]['sender'] == ''):
            res = []
        return res

    def msgViewer (self, res):
        res = res[0]
        msg = res['msg']
        msg = msg.replace('\t', '')

        forecolor = colorama.Back.CYAN
        reset = colorama.Back.RESET
        if (res['enemy'] == True):
            forecolor = colorama.Back.RED

        if (self.battle is False):
            print ('------------------------------')
            res['bar'] = '------------------------------'
        print (forecolor + ':' + reset + ' ' + res['sender'] + ' [' + res['mode'] + ']')
        print (msg)
        trans = Translator().translate(msg, dest = self.lang).text
        print (trans + '\r\n')
        res['trans'] = trans
        self.battle = True

        return json.dumps(res)

