import os
import codecs
import configparser

class Config:
    def __init__(self):
        inistr = ['[MAIN]', '\n', ';Refer to this page and specify the language code of the target language. (https://cloud.google.com/translate/docs/languages?hl=en)', '\n','lang=','en', '\n\n',';Display translation results in a browser? ( True or False ) ', '\n', ';Type in your browser to access(localhost:10101)', '\n','browse=','False', '\n\n',';Beep when you receive a chat ( True or False ) ', '\n','beep=','True', '\n\n', ';Translation using DeepL ( True or False )', '\n',';Uses browser language.', '\n','deepl=','True', '\n\n\n', '[PORT]', '\n','flask=','10101', '\n','websocket=','10102', '\n\n', '[IP]', '\n',';Allow access only to this IP address', '\n','host=','0.0.0.0']
        if not os.path.exists('./transthunder.ini'):
            self.iniEditor(inistr)
        params = self.iniReader()
        if (len(params) == 7):  #設定値の個数
            return
        
        for param in params:
            inistr[inistr.index(param + '=') + 1] = params[param]
        self.iniEditor(inistr)

    def iniEditor(self, inistr):
        f = open('./transthunder.ini', 'w')
        f.writelines(inistr)
        f.close()

    def iniReader(self):
        ini = configparser.SafeConfigParser()
        ini.readfp(codecs.open('./transthunder.ini', 'r', 'utf8'))

        params = {}
        for section in ini.sections():
            for key in ini[section]:
                params[key] = ini.get(section, key)
        return params
