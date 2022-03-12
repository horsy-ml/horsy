import sys
from modules.path import add_to_path, add_var
import urllib.request
import os
import threading
import ctypes
import winshell
from win32com.client import Dispatch
import pythoncom
import argparse

parser = argparse.ArgumentParser(description='horsy - the best package manager')
parser.add_argument('-p', '--path', action='store_true', help='path to install app', required=False,
                    default=os.path.expanduser("~") + "\horsy")
args = parser.parse_args()


def install():
    global args
    path_to_install = args.path
    if path_to_install == "":
        print("Please choose path to install")
        return
    if not os.path.exists(path_to_install):
        os.makedirs(path_to_install)
    if not os.path.exists(path_to_install + "\\apps"):
        os.makedirs(path_to_install + "\\apps")
    threads = list()
    print("Adding task to download horsy")
    threads.append(threading.Thread(target=urllib.request.urlretrieve,
                                    args=("https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe",
                                          os.path.join(path_to_install) + '/horsy.exe'), ))
    print("Adding task to download horsygui")
    threads.append(threading.Thread(target=urllib.request.urlretrieve,
                                    args=("https://github.com/horsy-ml/horsy/raw/master/bin/horsygui.exe",
                                          os.path.join(path_to_install) + '/horsygui.exe'), ))
    try:
        print("Starting tasks")
        for thread in threads:
            thread.start()
    except:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    print("Adding to PATH")
    add_var(path_to_install)
    add_to_path(os.path.join(path_to_install))
    print("Downloading version file")
    urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                               os.path.join(path_to_install) + '/apps/version')
    print("Version specified")

    def wait_for_finish():
        for thread in threads:
            thread.join()
        print("Downloading finished")
        print("Creating shortcuts")
        desktop = winshell.desktop()
        path = os.path.join(desktop, "horsy GUI.lnk")
        target = os.path.join(path_to_install) + '/horsygui.exe'
        wDir = os.path.join(path_to_install)
        icon = os.path.join(path_to_install) + '/horsygui.exe'
        pythoncom.CoInitializeEx(0)
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()
        print("Installation complete")

    threading.Thread(target=wait_for_finish).start()


if __name__ == '__main__':
    install()
