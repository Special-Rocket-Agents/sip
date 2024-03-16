import os
import sys
import urllib.request
import main
from main import *
import colorama

def run(importantFunctions, importantVars):
    print(f"""
{Fore.LIGHTBLUE_EX} ================== {Style.RESET_ALL}
{Fore.LIGHTBLUE_EX}|                  |{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}PyKern - The Python Kernel-alike{Fore.RESET}
{THISISLIGHTYELLOW}|  ######          |{Style.RESET_ALL} ================================
{THISISLIGHTYELLOW}|  #    #          |{Style.RESET_ALL} {Fore.CYAN}Installed Directory:{Fore.RESET} {osdir}
{Fore.LIGHTBLUE_EX}|  ######          |{Style.RESET_ALL} {Fore.CYAN}User:{Fore.RESET} {username}
{Fore.LIGHTBLUE_EX}|  #        #   #  |{Style.RESET_ALL} {Fore.CYAN}Curdir:{Fore.RESET} {curdir}
{THISISLIGHTYELLOW}|  #         # #   |{Style.RESET_ALL} {Fore.CYAN}Package Count:{Fore.RESET} {packagecount}
{THISISLIGHTYELLOW}|  #          #    |{Style.RESET_ALL} {Fore.CYAN}Package Manager:{Fore.RESET} SIP
{Fore.LIGHTBLUE_EX}|  #         #     |{Style.RESET_ALL} {Fore.CYAN}Superuser:{Fore.RESET} {su}
{Fore.LIGHTBLUE_EX}|                  |{Style.RESET_ALL} {Fore.CYAN}Operating System:{Fore.RESET} {os.name}
{THISISLIGHTYELLOW} ================== {Style.RESET_ALL}
        """)
    return