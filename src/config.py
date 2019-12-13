import os
import codecs
import configparser

class Config:
    def __init__(self):
        if not os.path.exists('./transthunder.ini'):
            f = open('./transthunder.ini', 'w')
            f.write('[MAIN]\nlang=en\n;Display translation results in a browser? ( True or False ) \nbrowse=False' + os.linesep +
            '[PORT]\nflask=10101\nwebsocket=10102' + os.linesep +'[IP]\n;IP address that allow access\nhost=0.0.0.0')
            f.close()

    def iniReader(self):
        ini = configparser.SafeConfigParser()
        ini.readfp(codecs.open('./transthunder.ini', 'r', 'utf8'))

        params = {}
        for section in ini.sections():
            for key in ini[section]:
                params[key] = ini.get(section, key)
        return params
