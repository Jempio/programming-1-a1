# mapit.py - launches a map in a
# browser using an address from the command line

import webbrowser
import sys
import pyperclip

prefix = "https://www.google.com/maps/place/"
# if there are arguments, use args as address
# if there are no arguments, grab from clipboard
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])

    webbrowser.open(prefix + address)

else:
    address = pyperclip.paste()
    webbrowser.open(prefix + address)


