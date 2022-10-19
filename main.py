# required modules
import tkinter as tk
from tkinter import filedialog
from subprocess import call
import pyfiglet

#banner logo QuickCopy
ascii_banner = pyfiglet.figlet_format("QuickCopy")

#introduction text
print(ascii_banner)
print("\033[1;32mWelcome to QuickCopy")
print("Version 1.0.0 (Demo)")
print("This program will make robocopy easy to use!")
print("Created by Jaymian-Lee Reinartz")
print("Github repository: https://github.com/Jaymian-Lee/robocopyplus \n")

#main code
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
        print("Thanks for using QuickCopy!")
        input("Press any key to exit")
        exit()
    else:
        print("Please enter a valid option")
        robocopyplus()

robocopyplus()

#restart code
def restartrobocopy():
    restart = input("Do you want to copy more files? (Y/N) ").lower()
    if restart == "y":
        robocopyplus()
    elif restart == "n":
        print("Thanks for using QuickCopy!")
        input("Press any key to exit")
        exit()
    else:
        print("Please enter a valid option")
        restartrobocopy()

restartrobocopy()