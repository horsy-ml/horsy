import requests
from PyQt5 import QtWidgets
import modules.gui as gui
from modules.auth import get_auth, del_auth
import modules.vars as horsy_vars
import json


def loginload():
    UiLoginWindow = QtWidgets.QMainWindow()
    login_ui = gui.Ui_LoginWindow()
    login_ui.setupUi(UiLoginWindow)
    try:
        with open(horsy_vars.horsypath + 'config.cfg') as f:
            config = json.load(f)
        if config['auth'] is not None:
            return (lambda x: (x if x != "Forbidden" else "Invalid login"))\
                (requests.get(horsy_vars.protocol + horsy_vars.server_url + '/users/login',
                              json={'auth': config['auth']}).json()['message'])
    except:
        pass


def login():
    UiLoginWindow = QtWidgets.QMainWindow()
    login_ui = gui.Ui_LoginWindow()
    login_ui.setupUi(UiLoginWindow)
    UiMainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(UiMainWindow)
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)
    try:
        if config['auth'] is not None:
            del_auth()
            gui.popup('Authentication', 'Auth deleted')
            return 'Log in first'
        else:
            raise 'No auth'
    except:
        print('It will return from login')
        print(get_auth(True, login_ui, QtWidgets.QMainWindow()))
