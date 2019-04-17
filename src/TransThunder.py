import requests
import json
from googletrans import Translator
from time import sleep
import re
import os
import colorama
from colorama import Back
import win_unicode_console

lang = 'en'
battle = False
def LangChecker():  #翻訳先の言語の設定
    global lang
    if (os.path.isfile('.\\TransThunder.txt')):
        with open ('.\\TransThunder.txt') as f:
            lang = f.readline()
            lang = lang.split(':')[1]
    else:
        with open ('.\\TransThunder.txt', 'w') as f:
            f.write('lang:en')
            lang = 'en'

def MsgChecker(lastId):   #翻訳するメッセージの選択
    res = []
    lastIdList = ['0', str(lastId)]
    for parameter in lastIdList:
        try:
            res = json.loads(requests.get('http://localhost:8111/gamechat?lastId=' + parameter).text)
        except:
            return res, lastId
        if (len(res) == 0):
            if (parameter == '0'):
                global battle
                battle = False
            return res, lastId

    lastId = res[0]['id']
    if (len(res) == 0 or re.search('<color=#\w*>', res[0]['msg']) or
        Translator().detect(res[0]['msg']).lang == lang or res[0]['sender'] == ''):
        res = []

    return res, lastId

def MsgViewer (res):
    msg = res[0]['msg']
    msg = msg.replace('\t', '')

    forecolor = Back.CYAN
    reset = Back.RESET
    if (res[0]['enemy'] == True):
        forecolor = Back.RED

    global battle
    if (battle is False):
        print ('------------------------------')
    print (forecolor + ':' + reset + ' ' + res[0]['sender'] + ' [' + res[0]['mode'] + ']')
    print (msg)
    print (Translator().translate(msg, dest = lang).text + '\r\n')
    battle = True

def Main():
    LangChecker()
    lastId = 0
    while (True):
        sleep(1)
        res, lastId = MsgChecker(lastId)
        if (len(res) == 0):
            continue

        MsgViewer(res)
        
if __name__ == '__main__':
    win_unicode_console.enable()
    colorama.init(autoreset=True)
    Main()

