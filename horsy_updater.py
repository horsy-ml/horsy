# Legacy, only if normal update method is not working
import argparse
import urllib.request
import threading
import ctypes
import sys
import os

parser = argparse.ArgumentParser(description='horsy updater')
parser.add_argument('option', nargs='?')
args = parser.parse_args()
option = args.option

path_to_install = os.popen('echo %HORSYPATH%').read().replace('\n', '')  # Get installation folder

if not os.path.exists(path_to_install):
    os.makedirs(path_to_install)
if not os.path.exists(path_to_install + "\\apps"):
    os.makedirs(path_to_install + "\\apps")
threads = list()
threads.append(threading.Thread(target=urllib.request.urlretrieve,
                                args=("https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe",
                                      os.path.join(path_to_install) + '/horsy.exe'), ))
if os.path.exists(path_to_install + '/horsygui.exe'):
    threads.append(threading.Thread(target=urllib.request.urlretrieve,
                                    args=("https://github.com/horsy-ml/horsy/raw/master/bin/horsygui.exe",
                                          os.path.join(path_to_install) + '/horsygui.exe'), ))
try:
    for thread in threads:
        thread.start()
except:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                           os.path.join(path_to_install) + '/apps/version')

for thread in threads:
    thread.join()

try:
    os.system(option)
except:
    input("horsy updated manually. You can launch it now. Press enter to exit.")
