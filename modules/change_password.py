import requests
import modules.gui as gui
from modules.auth import del_auth, get_auth
import modules.vars as horsy_vars
import json
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
        r = requests.put(horsy_vars.protocol + horsy_vars.server_url + '/users',
                         json={'auth': get_auth(True, login_ui, QtWidgets.QMainWindow()),
                               'password': newpass})
        try:
            r = r.json()
        except:
            if r.text == '':
                gui.popup('Success', 'Success, your password has been changed')
                with open(horsy_vars.horsypath + 'config.cfg') as f:
                    config = json.load(f)
                config['auth'] = {'email': config['auth']['email'], 'password': newpass}
                with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
                    json.dump(config, f)
        try:
            if r['message'] == 'Unauthorized':
                gui.popup('Error', 'Invalid credentials \nDeleting auth from config')
                del_auth()

            elif r['message'] == 'Internal server error':
                gui.popup('Error', 'Internal server error')
                return 'Internal server error'

            else:
                print('Unknown error, please try again')
                print('Server response:')
                print(r)
                return 'Unknown error, please try again, \n Server response: \n' + str(r)
        except:
            pass
    except:
        gui.popup('Error', 'Unexpected error.')
