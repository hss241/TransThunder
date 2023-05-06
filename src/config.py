import os
import codecs
import configparser

class Config:
    def __init__(self):
        inistr = ['[MAIN]', '\n', ';Refer to this page and specify the language code of the target language. (https://cloud.google.com/translate/docs/languages?hl=en)', '\n','lang=','en', '\n\n', ';Beep when you receive a chat ( True or False ) ', '\n','beep=','True', '\n\n\n', '[PORT]', '\n','browse_port=','10101']
        if not os.path.exists('./transthunder.ini'):
            self.iniEditor(inistr)
        params = self.iniReader()
        if (len(params) == 3):  #設定値の個数
            return
        
        for param in params:
            try:
                inistr[inistr.index(param + '=') + 1] = params[param]
            except:
                pass
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
