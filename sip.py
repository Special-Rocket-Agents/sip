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

import requests
def list_files_in_repo():
    url = f'https://api.github.com/repos/Special-Rocket-Agents/sip/contents/'
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.json()
        file_names = [item['name'] for item in content if item['type'] == 'file' and item['name'].endswith('.py')]
        return file_names

    else:
        print(f"Failed to list files. Status code: {response.status_code}")
        return []
def run(importantFunctions, importantVars):
    pakname = args[1]
    if pakname == "debug":
        print(f"OSDir: {osdir}")
        print(f"username: {username}")
        print(f"packagecount: {packagecount}")
        print(f"curdir: {curdir}")
        print(f"displayusername: {displayusername}")
        os.system("ping 8.8.8.8")
    elif pakname == "about":
        print(f""" 
░░      ░░        ░       ░░ SIP Package Manager
▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒ for PyKern, the Python Kernel-alike
▓▓      ▓▓▓▓▓  ▓▓▓▓       ▓▓ {Fore.GREEN}sip [package]{Fore.RESET} to install packages
███████  ████  ████  ███████ {Fore.RED}sip-uninstall [package]{Fore.RESET} to uninstall packages
██      ██        █  ███████ Repository: https://github.com/Special-Rocket-Agents/sip
                            
        """)
    elif pakname == "list":
        for i in list_files_in_repo():
            print(i)
    elif pakname == "help":
        print("""
SIP help list:
sip [package] - installs a package
sip about - shows about page
sip help - shows this
sip list - lists the packages available to download in the repository
        """)
    else:
        install_package(pakname, curdir, displayusername)
        setPath(osdir)
        return