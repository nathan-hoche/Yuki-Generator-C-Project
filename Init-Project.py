#!/usr/bin/env python3

import os
import json

from component import pcolors as pcolor

def import_config():
    with open("config.json") as fd:
        data = json.load(fd)
    return(data)

def get_file():
    data_file = []
    try:
        content = os.listdir("Data")
    except:
        print(pcolor.red + "Folder \"Data\" was delete" + pcolor.white)
        exit (0)
    for entry in content:
        if (entry.find(".c") != -1):
            data_file.append(entry)
    return data_file

def print_all_file(all_file):
    id_file = 0
    for act_file in all_file:
        print(str(id_file) + " : " + act_file)
        id_file += 1

def identify_file(choosen_file, data_file):
    lib = []
    for obj in choosen_file:
        lib.append(data_file[int(obj)])
    print(pcolor.blue + "LIB Content: " + str(lib) + pcolor.white)
    return lib

def Check_info(Name, Folder):
    try:
        os.listdir(Folder)
    except:
        print(pcolor.red + "Location doesn't exist" + pcolor.white)
        return (0)
    for entry in os.scandir(Folder):
        if entry.is_dir():
            if (entry.name == Name):
                print(pcolor.red + "Folder Already Exist" + pcolor.white)
                return 0
    print(pcolor.green + "ALL IS VALIDATE" + pcolor.white)
    return(1)

def Check_choosen_file(choosen_file, data_file):
    if (not choosen_file.replace(' ', '').replace('\n', '').isdigit()):
        print(pcolor.red + "Wrong character." + pcolor.white)
        print(pcolor.yellow + "Sample: \"0 1 3\"" + pcolor.white)
        return 0
    max_id = len(data_file) - 1
    array = choosen_file.split(' ')
    for nb in array:
        if (int(nb) > max_id):
            print(pcolor.red + "Wrong ID." + pcolor.white)
            return 0
    print(pcolor.green + "ALL IS VALIDATE" + pcolor.white)
    return 1
    

class Get_info():
    def __init__(self):
        self.name = None
        self.path = None
        self.config = import_config()
        self.lib = 1
        self.lib_choosen_file = []

    def lib_selection(self):
        if (self.config['Library'] and self.config['Library'] == 1):
            data_file = get_file()
            print(pcolor.blue + "----Library File----" + pcolor.white)
            print_all_file(data_file)
            check = 0
            while (check == 0):
                print(pcolor.blue + "Write all ID of file that you want in your library:" + pcolor.white)
                choosen_file = input()
                check = Check_choosen_file(choosen_file, data_file)
            self.lib_choosen_file = identify_file(choosen_file, data_file)
        else:
            print(pcolor.yellow + "Library Desactivate" + pcolor.white)
            self.lib = 0
    
    def launch_program(self):
        print(pcolor.blue + "----Starting Launchs----" + pcolor.white)

        check = 0
        while (check == 0):
            print("\nEnter The Project Name : ", end="")
            self.name = input()
            print("Enter The Project Location : ", end="")
            self.path = input()
            check = Check_info(self.name, self.path)
        print(pcolor.blue + "Project : " + self.name + " in location " + self.path + pcolor.white)


Info = Get_info()

Info.launch_program()
Info.lib_selection()