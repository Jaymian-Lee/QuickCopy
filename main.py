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
print("Github repository: https://github.com/Jaymian-Lee/quickcopy \n")


def optionfunc():
    
    # placeholder for the options variable
    options = "NOTSET"

    global options_list
    options_list = []
    
    # available options
    s = "/s"
    e = "/e"
    z = "/Z"
    b = "/b"
    zb = "/zb"
    j = "/j"

    # while loop to add options to a options_list
    while options != "":
        options = input("\nWhat copy options do you want to use? Press (H) for all commands! (press enter to continue) ").lower()
        if options == "h":
            print("     s = /s,  	Copies subdirectories. This option automatically excludes empty directories. \n" +
            "     e = /e 	Copies subdirectories. This option automatically includes empty directories. \n" +
            "     z = /z 	Copies files in restartable mode. In restartable mode, should a file copy be interrupted, Robocopy can pick up where it left off rather than recopying the entire file. \n" +
            "     b = /b, 	Copies files in backup mode. Backup mode allows Robocopy to override file and folder permission settings (ACLs). This allows you to copy files you might otherwise not have access to, assuming it's being run under an account with sufficient privileges. \n" + 
            "     zb = /zb 	Copies files in restartable mode. If file access is denied, switches to backup mode. \n" + 
            "     j = /j 	Copies using unbuffered I/O (recommended for large files).\n")
        elif options == "s":
            options_list.append(s)
        elif options == "e":
            options_list.append(e)
        elif options == "z":
            options_list.append(z)
        elif options == "b":
            options_list.append(b)
        elif options == "zb":
            options_list.append(zb)
        elif options == "j":
            options_list.append(j)

        # if input of options is equal to c exit the program
        elif options == "c":
            print("Thanks for using QuickCopy!")
            input("Press any key to exit")
            exit()

    print("Selected options: " + str(options_list))
    
# main code
def quickcopy():
    
    choice = input("Do you want to copy files or directory's? (F/D) \npress (C) to cancel ").lower()
    
    # if output of choice is equal to c then exit the program
    if choice == "c":
        print("Thanks for using QuickCopy!")
        input("Press any key to exit")
        exit()

    optionfunc()

    if choice == "d":

        # variables
        source = filedialog.askdirectory()
        destination = filedialog.askdirectory()

        print("Source: " + source)
        print("Destination: " + destination)

        print(options_list)
        # robocopy command example (/E)
        call(["robocopy",source, destination, "/E"])

    elif choice == "f":
        
        # variables
        source = filedialog.askopenfilename()
        destination = filedialog.askopenfilename()

        # print the output of the variables
        print("Source: " + source)
        print("Destination: " + destination)

        # import the options_list variable from the optionfunc function and print the outcome

        call(["robocopy",source, destination,"/D"])
    
    else:
        print("Please enter a valid option")
        quickcopy()


quickcopy()

# restart code from the beginning
def restartquickcopy():
    restart = input("Do you want to copy more files? (Y/N) ").lower()
    if restart == "y":
        quickcopy()
    elif restart == "n":
        print("Thanks for using QuickCopy!")
        input("Press any key to exit ")
        exit()
    else:
        print("Please enter a valid option")
        restartquickcopy()

restartquickcopy()