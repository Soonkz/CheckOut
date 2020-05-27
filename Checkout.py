import subprocess
import sys
from termcolor import colored
import os

def Impressum(repo):
    print(colored("+++++++++++++++++++++++++++++",'magenta'))
    print(colored('Running CheckOut - by SBO','yellow'))
    print(colored('https://github.com/Soonkz/CheckOut','yellow'))
    print(colored("+++++++++++++++++++++++++++++",'magenta'))
    
def checkOutput(convertedOutput):
    upToDate = "up to date"
    if convertedOutput.find(upToDate) != -1:
        print(colored("-----------------------------",'magenta'))
        print(colored('Repository already up to date','green'))
        print(colored("_____________________________",'magenta'))
    else: 
        print(colored("-----------------------------",'magenta'))
        print(colored('Repository needs update','red'))
        print(colored("_____________________________",'magenta'))

def changeRepo(name):
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    newPath = os.getcwd() + "\\" + name
    print(colored("switch to repository: " + newPath,'magenta'))
    os.chdir(newPath)

def gitStatus():
    print(colored('Perform git status','yellow'))
    return subprocess.run(["git", "status"], check=True,
                               stdout=subprocess.PIPE).stdout
def gitPull():
    print(colored('Perform git pull --ff-only','yellow'))
    return subprocess.run(["git", "pull", "--ff-only"], check=True,
                               stdout=subprocess.PIPE).stdout
def checkOutRepo(name):
    #git status command - return console output
    Impressum("Checkout")
    changeRepo(name)
    consoleOutput = gitStatus()
    convertedOutput = consoleOutput.decode("utf-8")
    checkOutput(convertedOutput)
    print(gitPull())
    
checkOutRepo("CheckOut")
#convert output to string




