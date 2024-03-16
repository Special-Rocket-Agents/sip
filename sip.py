# sip, the package installer
import os
import urllib.request
import main

def install_package(pkname, dir, username):
    try:
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Special-Rocket-Agents/sip/main/" + pkname + ".py", dir + "/user/" + username + "/pkg/" + pkname + ".py")
        print(f"Package '{pkname}' installed successfully!")
    except Exception as e:
        print(f"Error installing package '{pkname}': {e}")

if __name__ == "__main__":
    pkname = input("Enter the name of the package to install: ")
    install_package(pkname, dir, username)
