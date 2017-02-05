# programe Start with
# if mac os "! /sur/bin/env"
# if windows "#!python3"


# -*- coding:utf-8 -*-

#mcb.pyw - Saves and Loads pieces of text to the clip board
#Usage:
# py.exe mcb.pyw save <keyword> - Save clipboard to keyword
# py.exe mcb.pyw <keyword> - loads keyword to clipboard
# py.exe mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip,sys
import pprint

mcbShelf = shelve.open('mcb')

#Todo: Save clipboard content

if  len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print "save"


elif len(sys.argv) == 2 and sys.argv[1].lower() =="list":
    #Todo:List keywords
    pyperclip.copy(str(list(mcbShelf.keys())))
    print "list"

elif len(sys.argv) == 2:
    #Todo: load content
    pyperclip.copy(mcbShelf[sys.argv[1]])
    print "load"


mcbShelf.close()