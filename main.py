# required modules
import os
import tkinter as tk
from tkinter import filedialog
from subprocess import call

print("\033[1;32m\nWelcome to robocopy+")
print("Version 1.0.0 (Demo)")
print("This program will copy files from one directory to another")
print("Created by Jaymian-Lee Reinartz  \n")

    # D:\\OneDrive\\Bureaublad\\Test1\\fliet.txt


def robocopyplus():

    choice = input("Do you want to copy files or directory's? (F/D) \npress (C) to cancel ").lower()

    if choice == "d":

        # variables
        source = filedialog.askdirectory()
        destination = filedialog.askdirectory()

        print("Source: " + source)
        print("Destination: " + destination)

        call(["robocopy",source, destination,"/E"])


    elif choice == "f":
            # variables
        source = filedialog.askopenfilename()
        destination = filedialog.askopenfilename()

        print("Source: " + source)
        print("Destination: " + destination)

        call(["robocopy",source, destination,"/D"])
    
    elif choice == "c":
        print("Thanks for using robocopy+!")
        input("Press any key to exit")
        exit()
    else:
        print("Please enter a valid option")
        robocopyplus()

robocopyplus()

def restartrobocopy():
    restart = input("Do you want to copy more files? (Y/N) ").lower()
    if restart == "y":
        robocopyplus()
    elif restart == "n":
        print("Thanks for using robocopy+!")
        input("Press any key to exit")
        exit()
    else:
        print("Please enter a valid option")
        restartrobocopy()

restartrobocopy()