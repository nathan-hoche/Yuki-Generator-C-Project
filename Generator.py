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