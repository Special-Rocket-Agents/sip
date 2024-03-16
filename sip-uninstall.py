# sip-uninstall, the package remover
import os
import sys
import urllib.request
import main
import colorama
from main import *

def run(importantFunctions, importantVars):
    pakname = args[1]
    if pakname == "sip" or pakname == "sip-uninstall":
        print(f"{Fore.RED}Error{Fore.RESET} uninstalling package {Fore.YELLOW}'{pakname}'{Fore.RESET}: You are uninstalling an {Style.BRIGHT}essential package{Style.RESET_ALL}!")
        return
    try:
        os.remove(f"{osdir}/user/{username}/pkg/{pakname}.py")
        print(f"Package {Fore.YELLOW}'{pakname}'{Fore.RESET} uninstalled {Fore.GREEN}successfully!{Fore.RESET}")
    except FileNotFoundError:
        print(f"Package '{pakname}' not found.")
    except Exception as e:
        print(f"{Fore.RED}Error{Fore.RESET} uninstalling package {Fore.YELLOW}'{pakname}'{Fore.RESET}: {Style.BRIGHT}{e}{Style.RESET_ALL}")
    setPath(osdir)
    return
