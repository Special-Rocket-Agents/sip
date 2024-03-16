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
    elif pakname == "about":
        print(f"""

  {Fore.BLUE} ▄████████{Fore.RESET}  ▄█     ▄███████▄  SIP Package Uninstaller
  ███    ███ ███    ███    ███  for PyKern, the Python Kernel-alike
  ███    █▀  {Fore.YELLOW}███▌{Fore.RESET}   ███    ███  {Fore.GREEN}sip [package]{Fore.RESET} to install packages           
  ███        ███▌   ███    ███  {Fore.RED}sip-uninstall [package]{Fore.RESET} to uninstall packages
▀███████████ ███▌ ▀█████████▀   Repository: https://github.com/Special-Rocket-Agents/sip
         ███ ███    ███         If you want to reset PyKern's configurations
   ▄█    ███ ███    ███         you've come to the wrong place.
 ▄████████▀  █▀    ▄████▀       
                               
        """)
        pass
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
