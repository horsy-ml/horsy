import requests
import modules.gui as gui
from modules.auth import get_auth
import modules.vars as horsy_vars
from modules.http_status import handle
from PyQt5 import QtWidgets


def change(oldpass, newpass):
    UiLoginWindow = QtWidgets.QMainWindow()
    login_ui = gui.Ui_LoginWindow()
    login_ui.setupUi(UiLoginWindow)

    if oldpass == "" or newpass == "":
        gui.popup('Error', 'Please enter both old and new passwords.')
        return

    config = get_auth(True, gui.Ui_LoginWindow(), QtWidgets.QMainWindow())

    try:
        if oldpass != config['password']:
            gui.popup('Error', 'Old password does not match with password in config.cfg')
            return
    except:
        gui.popup('Error', 'You don\'t have a password set in config.cfg')
        return

    try:
        gui.cpopup("Changing password",
                   handle(requests.put(horsy_vars.protocol + horsy_vars.server_url + '/users',
                                       json={'auth': get_auth(True, login_ui, QtWidgets.QMainWindow()),
                                             'password': newpass}).status_code)[1])
    except:
        gui.popup('Error', 'Unexpected error.')
