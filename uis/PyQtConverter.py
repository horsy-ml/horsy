import os, easygui
from os.path import basename
slash = '/'

start = easygui.buttonbox("Open .ui file to convert it", "Converter", ("Browse file", "Cancel"))

if start == "Cancel":
    exit()

if start == "Browse file":
    thisFile = easygui.fileopenbox(filetypes=["*.ui"])

filename = basename(thisFile)[:-3]

os.system('python -m PyQt5.uic.pyuic -x ' + thisFile + " -o " + os.path.dirname(thisFile) + slash + filename + ".py")
