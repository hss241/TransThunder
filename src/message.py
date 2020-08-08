import requests
import json
from googletrans import Translator
from deepyl import DeepyL
import re
import os
import colorama
import win_unicode_console

class Message():
    def __init__(self, lang, accuracy):
        self.lang = lang
        self.battle = False
        self.lastId = 0
        if (accuracy == "True" and any(lang in item for item in ["ja","en","de","fr","es","pt","it","nl","pl","ru","zh"])):
            try:
                self.dl = DeepyL(lang)
            except:
                pass
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
            finally:
                if (len(res) == 0): #新規メッセージがない場合
                    if (parameter == '0'):  #試合していない場合
                        if (self.battle is True):
                            self.dl.close()
                        self.battle = False
                    return res

        self.lastId = res[0]['id']
        if (len(res) == 0 or re.search('<color=#\w*>', res[0]['msg']) or
            Translator().detect(res[0]['msg']).lang == self.lang or res[0]['sender'] == ''):
            res = ['receive']
        return res

    def viewer (self, res):        
        res = res[0]
        msg = res['msg']
        msg = msg.replace('\t', '')

        reset = colorama.Back.RESET
        team = colorama.Back.CYAN + ':' + reset + ' '
        if (res['enemy'] == True):
            team = colorama.Back.RED + ';' + reset + ' '

        if (self.battle is False):
            print ('------------------------------')
            res['bar'] = '------------------------------'
            self.dl.get()
        
        trans = ""
        if hasattr(self, "dl"):
            trans = self.dl.io(msg) #deepl, Firefox or Chrome
        if (msg == trans or trans == ""):   #deepl未対応言語だった場合
            trans = Translator().translate(msg, dest = self.lang).text  #googletrans

        print (team + res['sender'] + ' [' + res['mode'] + ']\r\n' + msg + '\r\n' + trans + '\r\n')
        res['trans'] = trans
        self.battle = True

        return json.dumps(res)