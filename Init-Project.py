#!/usr/bin/env python3

import sys
import os

from component import pcolors as pcolor

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

class Get_info():
    def __init__(self):
        self.name = None
        self.path = None
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



Get_info().launch_program()