import argparse
import subprocess
from modules.core.exception import hook
from modules.path import add_to_path
from ezzdl import dl
import urllib.request
import sys
import os

sys.excepthook = hook

parser = argparse.ArgumentParser(description='horsy installer')
parser.add_argument('--dir', help='install horsy to this directory')
args = parser.parse_args()

path = os.path.expanduser('~') + '\\horsy' if not args.dir else args.dir

if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(path + "\\apps"):
    os.makedirs(path + "\\apps")

dl(["https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe",
    "https://github.com/horsy-ml/horsy/raw/master/bin/horsygui.exe"],
   path)

print("Adding to PATH...")
add_to_path(path + "\\apps")
print("Success, added to PATH")

print("Downloading version file...")
urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                           path + '/apps/version')
print("Version specified")

print("Creating launch script...")
with open(path + "\\apps\\horsy.cmd", "w") as f:
    f.write(f'''@echo off
{path}\horsy.exe''')
with open(path + "\\apps\\horsygui.cmd", "w") as f:
    f.write(f'''@echo off
{path}\horsygui.exe''')
print("Success, created launch script")

print("Creating shortcut...")
with open('shortcut.vbs', 'w+') as f:
    f.write(f'''\
Set oWS = WScript.CreateObject("WScript.Shell")
user=oWS.ExpandEnvironmentStrings("%USERPROFILE%")
sLinkFile = user & "\Desktop\horsy GUI.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{path}/horsygui.exe"
oLink.Save
''')
subprocess.call('cscript /nologo shortcut.vbs')
os.remove('shortcut.vbs')
print("Success, created shortcut")

print()
print("Installation complete!")
