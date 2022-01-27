import argparse
import os
import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets

import modules.gui as gui
from modules.console import cls
import modules.vars as horsy_vars

# Initialize GUI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = gui.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

UiMainWindow = QtWidgets.QMainWindow()
login_ui = gui.Ui_LoginWindow()
login_ui.setupUi(UiMainWindow)


# Functions
def refresh_gui():
    installed_apps()

def installed_apps():
    from modules.manager import apps_list
    ui.installed_table.clear()
    apps = apps_list(True)
    ui.installed_table.setColumnCount(4)
    ui.installed_table.setRowCount(math.ceil(len(apps) / 4))
    for i in range(len(apps)):
        ui.installed_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(apps[i])))

def update_app():
    try:
        app_name = ui.installed_table.currentItem().text()
        if app_name == "":
            return
        else:
            from modules.manager import install
            install(app_name, True)
    except:
        return

def uninstall_app():
    try:
        app_name = ui.installed_table.currentItem().text()
        if app_name == "":
            return
        else:
            from modules.manager import uninstall
            uninstall(app_name)
            installed_apps()
    except:
        return

def search_gui():
    from modules.search import search
    search_query = ui.search_box.toPlainText()
    if search_query == "":
        return
    else:
        found = search(search_query, True)
        ui.search_table.clear()
        ui.search_table.setColumnCount(4)
        ui.search_table.setRowCount(math.ceil(len(found) / 4))
        for i in range(len(found)):
            ui.search_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(found[i])))

def install_app():
    from modules.manager import install
    try:
        app_name = ui.search_table.currentItem().text()
        if app_name == "":
            return
        else:
            install(app_name, True)
    except:
        return

def get_source_gui():
    from modules.source import get_source
    try:
        app_name = ui.search_table.currentItem().text()
        if app_name == "":
            return
        else:
            get_source(app_name)
    except:
        return


def upload_gui():
    from modules.uploader import upload
    upload(True, ui, login_ui)


# Run functions on startup
installed_apps()

# Binds
ui.tabWidget.currentChanged.connect(refresh_gui)
ui.update_button.clicked.connect(update_app)
ui.delete_button.clicked.connect(uninstall_app)
ui.search_button.clicked.connect(search_gui)
ui.install_button.clicked.connect(install_app)
ui.source_button.clicked.connect(get_source_gui)
ui.upload_button.clicked.connect(upload_gui)


# Handle GUI exiting to exit whole program
sys.exit(app.exec_())
