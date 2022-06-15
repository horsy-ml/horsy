import subprocess
from ui.installer import Ui_MainWindow
from modules.core.exception import hook, thread_hook
from ui.modules.popup import popup
from modules.path import add_to_path
from modules.core.qt_updater import call
from modules.gui.downloader import download_url
from PyQt5 import QtWidgets, QtGui
from ezzthread import threaded
import urllib.request
import threading
import sys
import os

sys.excepthook = hook
threading.excepthook = thread_hook

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.progressBar.hide()


def open_dir():
    global ui
    ui.install_horsygui_button.setEnabled(False)
    path = str(os.path.join(QtWidgets.QFileDialog.getExistingDirectory(caption='Installation folder')) + "\horsy")\
        .replace("/", "\\").replace('\\\\', '\\')
    ui.path_box.setText(path)


def check_is_installed():
    global ui
    if os.path.isfile(ui.path_box.text() + "\\horsy.exe"):
        ui.install_horsygui_button.setEnabled(True)
        popup('Info', 'horsy is already installed in this folder, you can modify it if you want.')
    else:
        ui.install_horsygui_button.setEnabled(False)


@threaded
def install_horsy(*args):
    global ui
    call(ui.logsBrowser.clear)
    call(ui.install_horsy_button.setEnabled, False)
    call(ui.path_box.setEnabled, False)
    call(ui.choose_path_button.setEnabled, False)
    if ui.path_box.text() == "":
        popup("Error", "Please select a folder to install horsy to")
        return

    if not os.path.exists(ui.path_box.text()):
        os.makedirs(ui.path_box.text())
    if not os.path.exists(ui.path_box.text() + "\\apps"):
        os.makedirs(ui.path_box.text() + "\\apps")

    call(ui.logsBrowser.append, "Downloading horsy...")
    call(ui.progressBar.show)
    download_url(ui.progressBar, None, "https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe",
                 ui.path_box.text() + "\\horsy.exe")
    call(ui.logsBrowser.append, "Success, downloaded")
    call(ui.progressBar.hide)

    call(ui.logsBrowser.append, "Adding to PATH...")
    add_to_path(ui.path_box.text() + "\\apps")
    call(ui.logsBrowser.append, "Success, added to PATH")

    call(ui.logsBrowser.append, "Downloading version file...")
    urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                               ui.path_box.text() + '/apps/version')
    call(ui.logsBrowser.append, "Version specified")

    call(ui.logsBrowser.append, "Creating launch script...")
    with open(ui.path_box.text() + "\\apps\\horsy.cmd", "w") as f:
        f.write(f'''@echo off
{ui.path_box.text()}\horsy.exe''')
    call(ui.logsBrowser.append, "Success, created launch script")

    call(ui.logsBrowser.append, "")
    call(ui.logsBrowser.append, "Installation complete!")
    call(ui.logsBrowser.moveCursor, QtGui.QTextCursor.End)
    call(ui.install_horsy_button.setEnabled, True)
    call(ui.install_horsygui_button.setEnabled, True)


@threaded
def install_horsygui(*args):
    global ui
    call(ui.logsBrowser.clear)
    call(ui.install_horsygui_button.setEnabled, False)
    if ui.path_box.text() == "":
        popup("Error", "Please select a folder to install horsygui to")
        return

    if not os.path.exists(ui.path_box.text()):
        os.makedirs(ui.path_box.text())
    if not os.path.exists(ui.path_box.text() + "\\apps"):
        os.makedirs(ui.path_box.text() + "\\apps")

    call(ui.logsBrowser.append, "Downloading horsygui...")
    call(ui.progressBar.show)
    download_url(ui.progressBar, None, "https://github.com/horsy-ml/horsy/raw/master/bin/horsygui.exe",
                 ui.path_box.text() + "\\horsygui.exe")
    call(ui.logsBrowser.append, "Success, downloaded")
    call(ui.progressBar.hide)

    call(ui.logsBrowser.append, "Adding to PATH...")
    add_to_path(ui.path_box.text() + "\\apps")
    call(ui.logsBrowser.append, "Success, added to PATH")

    call(ui.logsBrowser.append, "Downloading version file...")
    urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                               ui.path_box.text() + '/apps/version')
    call(ui.logsBrowser.append, "Version specified")

    call(ui.logsBrowser.append, "Creating launch script...")
    with open(ui.path_box.text() + "\\apps\\horsygui.cmd", "w") as f:
        f.write(f'''@echo off
{ui.path_box.text()}\horsygui.exe''')
    call(ui.logsBrowser.append, "Success, created launch script")

    call(ui.logsBrowser.append, "Creating shortcut...")
    with open('shortcut.vbs', 'w+') as f:
        f.write(f'''\
Set oWS = WScript.CreateObject("WScript.Shell")
user=oWS.ExpandEnvironmentStrings("%USERPROFILE%")
sLinkFile = user & "\Desktop\horsy GUI.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{ui.path_box.text()}/horsygui.exe"
oLink.Save
''')
    subprocess.call('cscript /nologo shortcut.vbs')
    os.remove('shortcut.vbs')
    call(ui.logsBrowser.append, "Success, created shortcut")

    call(ui.logsBrowser.append, "")
    call(ui.logsBrowser.append, "Installation complete!")
    call(ui.logsBrowser.moveCursor, QtGui.QTextCursor.End)
    call(ui.install_horsygui_button.setEnabled, True)


ui.path_box.setText(os.path.expanduser('~') + '\\horsy')
check_is_installed()

MainWindow.show()

ui.choose_path_button.clicked.connect(open_dir)
ui.install_horsy_button.clicked.connect(install_horsy)
ui.install_horsygui_button.clicked.connect(install_horsygui)
ui.path_box.textChanged.connect(check_is_installed)

sys.exit(app.exec_())
