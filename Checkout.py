import subprocess
import sys
from termcolor import colored
import colorama
import os
import json

os.system('color')

    
def Impressum(repo):
    print(colored("+++++++++++++++++++++++++++++\n",'magenta'))
    print(colored('>> Running CheckOut - by SBO << ','yellow'))
    print(colored('>> Follow on Github          <<','yellow'))
    print(colored('>> https://github.com/Soonkz/CheckOut <<\n','yellow'))
    print(colored("+++++++++++++++++++++++++++++\n",'magenta'))

def successfull():
    print(colored("\n^^^^^^^^^^^^^^^^^^^^^^^^",'green'))
    print(colored("Checkout has run successfully!",'green'))
    print(colored("^^^^^^^^^^^^^^^^^^^^^^^^",'green'))

def gitStatus():
    print(colored('>> Perform git status <<','yellow'))
    return subprocess.run(["git", "status"], check=True,
                               stdout=subprocess.PIPE,shell=True).stdout
def gitPull():
    print(colored('>> Perform git pull --ff-only <<','yellow'))
    try:
        value = subprocess.run(["git", "pull", "--ff-only"], check=True,
                               stdout=subprocess.PIPE,shell=True).stdout
        if value is 128:
            print(colored("Failed to pull: ",'red'))
        else:
            return value
    except ValueError as e:
        print(colored("Error" + e,'red'))

def gitCheckOutBranch(branchOrTag):
    print(colored('>> Perform git checkout - BranchOrTag:' + branchOrTag + ' <<','yellow'))
    try:
        maybeOutput =  subprocess.run(["git", "checkout",branchOrTag], check=True,stdout=subprocess.PIPE,shell=True).stdout
        return maybeOutput
    except ValueError as e:
        print(colored("Error" + e,'red'))

    
def checkOutput(consoleOutput,operation,branchname,repo):
    convertedOutput = consoleOutput.decode("utf-8")
    if operation is "status":
        upToDate = "up to date"
        nothing = "working tree clean"
        ahead = "Your branch is ahead"
        if convertedOutput.find(upToDate) != -1:
            print(colored('Repository already up to date','green'))
            return
        if convertedOutput.find(nothing) != -1:
            print(colored('nothing to commit, working tree clean','green'))
            return
        if convertedOutput.find(ahead) != -1:
            print(colored('your branch is ahead but can perform pull','white'))
            return
        else: 
            print(colored('Stash or commit your changes','red'))
            sys.exit()
    #if operation is "checkout":
        #alreadyOnBranchTag = "Already on"
        #if convertedOutput.find(alreadyOnBranchTag):
        #    print(colored('Already on \"' + branchname + '\"','green'))
        #else:
        #    print(colored('Checkout \"' + branchname + '\"','white'))

    if operation is "pull":
        alreadyPulled = "Already up to"
        unrelatedHistory = "refusing to merge unrelated histories"
        if convertedOutput.find(alreadyPulled) != -1:
            print(colored('Branch: \"' + branchname + '\" is already up to date','green'))
            return
        if convertedOutput.find(unrelatedHistory) != -1:
            print(colored('fatal: refusing to merge unrelated histories\n','red'))
            sys.exit()
        else:
            print(colored("Fast Forward Pull successfully performed"))

def changeRepo(name):
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    newPath = os.getcwd() + "\\" + name
    print(colored("switch to repository: " + newPath,'magenta'))
    os.chdir(newPath)


def checkOutRepo(name,branchOrTag,branchName):

    #Switch to the specific git repository
    changeRepo(name)

    #Check for unsaved changes before checkout the branch/tag - git status 
    consoleOutput = gitStatus()
    checkOutput(consoleOutput, "status", branchName, name)

    #Checkout the correct branch or tag
    consoleOutput = gitCheckOutBranch(branchName)
    checkOutput(consoleOutput, "checkout", branchName, name)

    #git pull --ff-only / Fast forward only
    consoleOutput = gitPull()
    checkOutput(consoleOutput, "pull", branchName, name)


Impressum("Checkout")
with open('CheckOut.json') as json_file:
    try:
        data = json.load(json_file)
        for repo in data['Repositories']:
            checkOutRepo(repo['Name'],repo['BranchOrTag'],repo['BranchName'])
            print(colored('-------------------------------------------\n','magenta'))
    except ValueError as e:
        print(colored("Invalid Json - check CheckOut.json file!",'red'))
successfull()




