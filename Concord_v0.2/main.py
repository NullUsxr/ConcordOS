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
nopass = 1
print("Searching File System...")
os.getcwd()
lsdir = os.listdir()
workingdir = os.getcwd()
print("Defining Color Scheme...")
print("\x1b[37mDefined Color Scheme!")


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
            cliinput = userinput.lower()
            if cliinput == "clear":
                print('\n' * 150)
                validcmd = 1
            if cliinput == "exit":
                validcmd = 1
                exit()
            if cliinput == "color":
                validcmd = 1
                print("=== TERMINAL TEXT COLOR ===")
                print("\x1b[37m[1]\x1b[31m Red")
                print("\x1b[37m[2]\x1b[32m Green")
                print("\x1b[37m[3]\x1b[34m Blue")
                print("\x1b[37m[4]\x1b[36m Cyan")
                print("\x1b[37m[5]\x1b[35m Magenta")
                print("\x1b[37m[6]\x1b[33m Yellow")
                print("\x1b[37m[7]\x1b[37m White")
                print("\x1b[37m[8]\x1b[30m Black")
                print("\x1b[37m")
                userinput = input(commandparamater)
                if userinput.lower() == "1":
                    print("\x1b[31mColor Changed!")
                    currentcolor = "red"
                    nopass = 0
                if userinput.lower() == "2":
                    print("\x1b[32mColor Changed!")
                    currentcolor = "green"
                    nopass = 0
                if userinput.lower() == "3":
                    print("\x1b[34mColor Changed!")
                    currentcolor = "blue"
                    nopass = 0
                if userinput.lower() == "4":
                    print("\x1b[36mColor Changed!")
                    currentcolor = "cyan"
                    nopass = 0
                if userinput.lower() == "5":
                    print("\x1b[35mColor Changed!")
                    currentcolor = "magenta"
                    nopass = 0
                if userinput.lower() == "6":
                    print("\x1b[33mColor Changed!")
                    currentcolor = "yellow"
                    nopass = 0
                if userinput.lower() == "7":
                    print("\x1b[37mColor Changed!")
                    currentcolor = "white"
                    nopass = 0
                if userinput.lower() == "8":
                    print("\x1b[30mColor Changed!")
                    currentcolor = "black"
                    nopass = 0
                if nopass == 1:
                    print("Invalid selection!")
            if cliinput == "about":
                validcmd = 1
                print("=== ABOUT THIS DEVICE ===")
                print("OS:", sysname)
                print("OS Version:", sysver)
                print("OS Release:", sysrelease)
                print()
                print("Username:", osusername)
                print("Session:", usersession)
                print("Root:", isrooted)
            if cliinput == "restart":
                validcmd = 1
                print("Restarting...")
                print()
                os.execv(sys.executable, ['python'] + sys.argv)
            if cliinput == "list":
                validcmd = 1
                print("=== LISTING DIRECTORY OF", workingdir, "===")
                print(lsdir)
            if cliinput == "cd":
                validcmd = 1
                print("Currently in:", workingdir)
            if cliinput == "colortest":
                validcmd = 1
                colortest = "\x1b[34m BLUE \x1b[31m RED \x1b[37m WHITE \x1b[32m GREEN "
                colortest2 = "\x1b[30m BLACK \x1b[36m CYAN \x1b[33m YELLOW \x1b[35m MAGENTA"
                print(colortest, colortest2)
            if cliinput == "help":
                validcmd = 1
                print("=== HELP ===")
                print("ABOUT: Displays device information")
                print("CD: Displays the current directory")
                print("CLEAR: Clears the screen")
                print("COLOR: Change the Terminal color")
                print("EXIT: Exits")
                print("HELP: Displays this page")
                print("LIST: Lists files in the working directory")
                print("RESTART: Restarts the system")
            if validcmd == 0:
                print("\x1b[33m", cliinput, "\x1b[31mis not a known command! Type help for commands.\x1b[37m")
            print()
except():
    print("\x1b[31mAn unexpected error occurred!\x1b[37m")
