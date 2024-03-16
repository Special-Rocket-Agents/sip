# sip, the package installer
import os
import sys
import urllib.request
import main
from main import *

def install_package(pkname, dir, username):
    try:
        paakname = urllib.request.urlretrieve("https://raw.githubusercontent.com/Special-Rocket-Agents/sip/main/" + pkname + ".py", osdir + "/user/" + username + "/pkg/" + pkname + ".py")
        print(f"Package '{pkname}' installed successfully!")
    except Exception as e:
        print(f"Error installing package '{pkname}': {e}")

def run(importantFunctions, importantVars):
    pakname = args[1]
    if pakname == "debug":
        print(f"OSDir: {osdir}")
        print(f"username: {username}")
        print(f"packagecount: {packagecount}")
        print(f"curdir: {curdir}")
        print(f"displayusername: {displayusername}")
    else:
        install_package(pakname, curdir, displayusername)
    return
