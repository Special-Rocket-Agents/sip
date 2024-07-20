# Super Installer Package
This is the package repository for Pykern, the simulated kernel.

Pull requests are allowed but my reviewing is required to avoid malice.

You can upload new package files (by moderation) and you can modify the existing packages to only add features or make it more efficient.

## API
Consider reading the other accepted packages.

It's generally like this

```py
import os
import sys
import urllib.request
import main
from main import *
import colorama

def run(importantFunctions, importantVars):
# The juicy stuff is here.
# Pykern WILL look for this and call this. If you need functions, code it above run(). Most of main.py can be accessed.
# Arguments are available to you. args[*]. Don't forget the fact that arguments can be omitted. It will IndexError if not programmed correctly.
```
