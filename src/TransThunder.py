import requests
import json
from googletrans import Translator
from time import sleep
import re
import os
import colorama
from colorama import Back

def LangChecker(lang):  #翻訳先の言語の設定
    if (os.path.isfile('.\\TransThunder.txt')):
        with open ('.\\TransThunder.txt') as f:
            lang = f.readline()
            lang = lang.split(':')[1]
    else:
        with open ('.\\TransThunder.txt', 'w') as f:
            f.write('lang:en')
    return lang

def MsgChecker(lastId, lang):   #翻訳するメッセージの選択
    res = []
    try:
        res = json.loads(requests.get('http://localhost:8111/gamechat?lastId=0').text)
    except:
        return res, lastId
    if (len(res) == 0):
        lastId = 0
        return res, lastId
        
    try:
        res = json.loads(requests.get('http://localhost:8111/gamechat?lastId=' + str(lastId)).text)
    except:
        return res, lastId
    if (len(res) == 0):
        return res, lastId

    if (lastId == 0):
            print ('------------------------------')
            
    lastId = res[0]['id']
    
    if (len(res) == 0 or re.search('<color=#\w*>', res[0]['msg']) or
        Translator().detect(res[0]['msg']).lang == lang or res[0]['sender'] == ''):
        res = []
        
    return res, lastId

def Main():
    lang = 'en'
    lastId = 0

    lang = LangChecker(lang)
    while (True):
        sleep(1)
        
        res, lastId = MsgChecker(lastId, lang)
        if (len(res) == 0):
            continue
        
        msg = res[0]['msg']
        msg = msg.replace('\t', '')

        forecolor = Back.CYAN
        reset = Back.RESET
        if (res[0]['enemy'] == True):
            forecolor = Back.RED

        try:
            print (forecolor + ':' + reset + ' ' + res[0]['sender'] + ' [' + res[0]['mode'] + ']')
        except:
            print (forecolor + ':' + reset + ' ??? [' + res[0]['mode'] + ']')

        try:
            print (msg)
        except:
            print ('???')

        try:
            print (Translator().translate(msg, dest = lang).text + '\r\n')
        except:
            print ('???')

        
            
if __name__ == '__main__':
    colorama.init(autoreset=True)
    Main()

