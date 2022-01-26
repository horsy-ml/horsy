import argparse
import os
import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets

import modules.gui as gui
from modules.console import cls
from modules.virustotal import add_to_cfg
from modules.uploader import upload
from modules.source import get_source
from modules.search import search, info
import modules.vars as horsy_vars

# Initialize GUI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = gui.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# Functions
def installed_apps():
    from modules.manager import apps_list
    ui.installed_table.clear()
    apps = apps_list(True)
    ui.installed_table.setColumnCount(4)
    ui.installed_table.setRowCount(math.ceil(len(apps) / 4))
    for i in range(len(apps)):
        ui.installed_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(apps[i])))

def update_app():
    app_name = ui.installed_table.currentItem().text()
    if app_name == "":
        return
    else:
        from modules.manager import install
        install(app_name)

def uninstall_app():
    app_name = ui.installed_table.currentItem().text()
    if app_name == "":
        return
    else:
        from modules.manager import uninstall
        uninstall(app_name)
        installed_apps()

# Run functions on startup
installed_apps()

# Binds
ui.update_button.clicked.connect(update_app)
ui.delete_button.clicked.connect(uninstall_app)


# Handle GUI exiting to exit whole program
sys.exit(app.exec_())
