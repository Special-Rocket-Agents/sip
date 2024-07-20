#! /usr/bin/env python
import os
import sys
import urllib.request
import main
from main import *
import colorama
import curses
import shutil

def launch_menu():
    screen = curses.initscr()   # Initialize a new Windowobject which reprents the whole screen
    curses.noecho()             # Turn off the echo mode
    curses.curs_set(0)          # Leave cursor invisible
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Initialize a color-pair with RED as fg and WHITE as bg
    screen.keypad(1)
    selection = -1
    option = 0
    #curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    while selection < 0:
        screen.clear()
        h = [0] * 5 # curses.A_NORMAL = 0
        h[option] = curses.color_pair(1)
        #h[option] = curses.A_REVERSE
        screen.addstr(2, 4, "Kernel Setup for PyKern")
        screen.addstr(2, 4, "Pre-alpha - Under construction")
        screen.addstr(4, 4, "Please select an option...", curses.A_BOLD)
        screen.addstr(5, 4, "1 - Reinstall", h[0])
        screen.addstr(6, 4, "2 - Nothing", h[1])
        screen.addstr(7, 4, "3 - Nothing", h[2])
        screen.addstr(8, 4, "4 - Nothing", h[3])
        screen.addstr(9, 4, "5 - Exit ('q')", h[4])
        screen.refresh()
        q = screen.getch()
        if q == curses.KEY_UP or q == ord('k'):      # KEY_UP or 'k' on vim mode
            option = (option - 1) % 5
        elif q == curses.KEY_DOWN or q == ord('j'):  # KEY_DOWN or 'j' on vim mode
            option = (option + 1) % 5
        elif q == ord('\n'):
            selection = option
        if q == ord('q') or selection == 4:  # If 'q' or select 'Exit', then quit
            break
    
    curses.endwin()
    if selection == 0:
        print("This is your last chance to revise. If there is anything that needs backup. Do NOT press Enter. Ctrl + C out of this mess!")
        input("Are you sure? [ENTER/RETURN]")
        shutil.rmtree(osdir)
        os.remove('config.pykern')
        print(f"{red}The Pykern directory and configuration file have been deleted. Restarting the script should initiate the setup screen. Type exit now.{reset}")
def run(importantFunctions, importantVars):
    # -*- coding: utf-8 -*-
    launch_menu()