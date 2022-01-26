import argparse
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import modules.gui as gui
from modules.console import cls
from modules.manager import install, uninstall, apps_list
from modules.virustotal import add_to_cfg
from modules.uploader import upload
from modules.source import get_source
from modules.search import search, info
import modules.vars as horsy_vars


# Functions


# Initialize GUI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = gui.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Binds


# Handle GUI exiting to exit whole program
sys.exit(app.exec_())
