import os
import sys
import time


print("Starting Concord...")
print("Defining Variables...")
osusername = "admin"
validcmd = 0
sysname = "Concord"
sysver = "v0.2"
sysrelease = "2022"
commandparamater = "#>"
print("Searching File System...")
os.getcwd()
lsdir = os.listdir()
workingdir = os.getcwd()
print("Primed to start User Session!")
usersession = 1
if usersession == 1:
    rootprivileges = 1
    isrooted = "yes"
else:
    rootprivileges = 0
    isrooted = "no"
time.sleep(1)
print("Clearing Screen...")
print('\n' * 150)
try:
    class Clistart:
        print(sysname, sysver, sysrelease)
        print(time.strftime("%D %A %H:%M:%S"))
        print("Welcome,", osusername)
        print()


    while 1:
        class Userinput:
            validcmd = 0
            userinput = input(commandparamater)
            if userinput.lower() == "clear":
                print('\n' * 150)
                validcmd = 1
            if userinput.lower() == "exit":
                validcmd = 1
                exit()
            if userinput.lower() == "about":
                validcmd = 1
                print("=== ABOUT THIS DEVICE ===")
                print("OS:", sysname)
                print("OS Version:", sysver)
                print("OS Release:", sysrelease)
                print()
                print("Username:", osusername)
                print("Session:", usersession)
                print("Root:", isrooted)
            if userinput.lower() == "restart":
                validcmd = 1
                print("Restarting...")
                print()
                os.execv(sys.executable, ['python'] + sys.argv)
            if userinput.lower() == "list":
                validcmd = 1
                print("=== LISTING DIRECTORY OF", workingdir, "===")
                print(lsdir)
            if userinput.lower() == "cd":
                validcmd = 1
                print("Currently in:", workingdir)
            if userinput.lower() == "help":
                validcmd = 1
                print("=== HELP ===")
                print("ABOUT: Displays device information")
                print("CD: Displays the current directory")
                print("CLEAR: Clears the screen")
                print("EXIT: Exits")
                print("HELP: Displays this page")
                print("LIST: Lists files in the working directory")
                print("RESTART: Restarts the system")
            if validcmd == 0:
                print(userinput, "is not a known command!")
            print()
except():
    print("An unexpected error occurred!")
