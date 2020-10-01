import os

from component import pcolors as pcolor

class Generator():
    def __init__(self):
        self.name = None
        self.path = None
        self.project = None

    def create_all_directories(self):
        if (self.path[len(self.path) - 1] != '/'):
            self.path += "/"
        try:
            os.mkdir(self.path + self.name)
            self.project = self.path + self.name
        except OSError:
            print(pcolor.red + "Creation of Project failed" + pcolor.white)
            print(pcolor.yellow + "Try to change Location" + pcolor.white)
            exit (0)

    def init_generator(self, name, path):
        self.name = name
        self.path = path