import argparse
import os
import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets

import modules.gui as gui
from modules.console import cls
from modules.manager import install, uninstall, apps_list
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
    apps = apps_list(True)
    ui.installed_table.setColumnCount(4)
    ui.installed_table.setRowCount(math.ceil(len(apps) / 4))
    for i in range(len(apps)):
        ui.installed_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(apps[i])))


# Run functions on startup
installed_apps()

# Binds


# Handle GUI exiting to exit whole program
sys.exit(app.exec_())
