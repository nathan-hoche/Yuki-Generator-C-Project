import os
import shutil

from component import pcolors as pcolor
from component import Config

class Generator():
    def __init__(self):
        self.name = None
        self.path = None
        self.project = None
        self.config = None

    def cp_lib(self, lib_choosen):
        for file_name in lib_choosen:
            shutil.copy("Data/" + file_name, self.project + "/lib")

    def add_makefile(self):
        fd = open("Data/Makefile", 'r')
        content = fd.read().split("\n")
        fd.close()
    
        nb_line = 0
        for line in content:
            print("P" + line + "P")
            if (line == None or line == ""):
                content[nb_line] = ""
            elif (line[0] == '#'):
                content[nb_line] = None
            elif (not line.find("SRC\t=")):
                content[nb_line] = line + "\t" + self.config.get_main_file() + ".c"
            elif (not line.find("FLAGS\t=")):
                content[nb_line] = line + "\t" + self.config.get_flags()
            elif (line == "\t\t$(MAKE_LIB)" and self.config.get_lib() == 0):
                content[nb_line] = None
            nb_line += 1
        fd = open(self.project + "/Makefile", "x")
        for line in content:
            if (line != None):
                fd.write(line + "\n")
        fd.close()

    def create_all_directories(self):
        if (self.path[len(self.path) - 1] != '/'):
            self.path += "/"
        try:
            os.mkdir(self.path + self.name)
            self.project = self.path + self.name
            if (self.config.get_src_folder() == 1):
                os.mkdir(self.project + "/src")
            if (self.config.get_lib() == 1):
                os.mkdir(self.project + "/lib")
            if (len(self.config.get_include()) != 0):
                os.mkdir(self.project + "/include")
        except OSError:
            print(pcolor.red + "Creation of folder failed" + pcolor.white)
            print(pcolor.yellow + "Try to change Location" + pcolor.white)
            exit(0)

    def init_generator(self, name, path, config):
        self.name = name
        self.path = path
        self.config = config