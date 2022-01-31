import requests
import modules.gui as gui
import threading
from modules.auth import del_auth
import modules.vars as horsy_vars
import json
from PyQt5 import QtWidgets


def change(oldpass, newpass):
    ui = gui.Ui_MainWindow()
    ui.setupUi(QtWidgets.QMainWindow())

    if oldpass == "" or newpass == "":
        gui.popup('Error', 'Please enter both old and new passwords.')
        return

    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    try:
        if oldpass != config['auth']['password']:
            gui.popup('Error', 'Old password does not match with password in config.cfg')
            return
    except KeyError:
        gui.popup('Error', 'You don\'t have a password set in config.cfg')
        return

    try:
        r = requests.put(horsy_vars.protocol + horsy_vars.server_url + '/users',
                         json={'auth': config['auth'], 'password': newpass}).text
        try:
            if r['message'] == 'Unauthorized':
                gui.popup('Error', 'Invalid credentials \nDeleting auth from config')
                del_auth()

            elif r['message'] == 'Internal server error':
                gui.popup('Error', 'Internal server error')
                return 'Internal server error'

            elif r == '':
                gui.popup('Success', 'Success, your password has been changed')

            else:
                print('[red]Unknown error, please try again[/red]')
                print('Server response:')
                print(r)
                return 'Unknown error, please try again, \n Server response: \n' + str(r)
        except:
            pass
    except:
        gui.popup('Error', 'Unexpected error.')
