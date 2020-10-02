import json

class pcolors:
    pink = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def import_config():
    with open("config.json") as fd:
        data = json.load(fd)
    return(data)

class Config():
    def __init__(self):
        self.config = import_config()
        self.include = []
        self.main_file = None
        self.make_option = ""
        self.src_folder = 1
        self.lib = 1

    def get_lib(self):
        return self.lib

    def get_src_folder(self):
        return self.src_folder

    def get_include(self):
        return self.include

    def set_config(self):
        try:
            self.lib = self.config['Library']
            for option in self.config['Makefile-Option']:
                if option['activate'] == 1:
                    self.make_option += " " + option['option']
            self.src_folder = self.config['Src-folder']
            if (self.config['main-file']['activate'] == 1):
                self.main_file = self.config['main-file']['name']
            if (self.config['Include']['activate'] == 1):
                print("add in include")
                self.include.append(self.config['Include']['name'])
                self.include.append(self.config['Include']['protection'])
                print(self.include)
        except:
            print(pcolors.red + "Config JSON invalid." + pcolors.white)
            return 1
        return 0