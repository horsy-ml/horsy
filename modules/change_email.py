import requests
import modules.gui as gui
from modules.auth import del_auth, get_auth
import modules.vars as horsy_vars
import json
import threading
from PyQt5 import QtWidgets


def change(email):
    UiLoginWindow = QtWidgets.QMainWindow()
    login_ui = gui.Ui_LoginWindow()
    login_ui.setupUi(UiLoginWindow)

    if email == "":
        gui.popup('Error', 'Please enter new email address')
        return

    auth = get_auth(True, login_ui, QtWidgets.QMainWindow())

    try:
        def change_in_new_thread():
            try:
                r = requests.put(horsy_vars.protocol + horsy_vars.server_url + '/users',
                                 json={'auth': auth, 'email': email})
                try:
                    r = r.json()
                except:
                    if r.text == '':
                        gui.cpopup('Success', 'Success, your email has been changed')
                        with open(horsy_vars.horsypath + 'config.cfg') as f:
                            config = json.load(f)
                        config['auth'] = {'email': email, 'password': config['auth']['password']}
                        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
                            json.dump(config, f)
                try:
                    if r['message'] == 'Unauthorized':
                        gui.cpopup('Error', 'Invalid credentials \nDeleting auth from config')
                        del_auth()

                    elif r['message'] == 'Internal server error':
                        gui.cpopup('Error', 'Internal server error')
                        return 'Internal server error'

                    else:
                        print('Unknown error, please try again')
                        print('Server response:')
                        print(r.text)
                        return 'Unknown error, please try again, \n Server response: \n' + str(r.text)
                except:
                    pass
            except:
                gui.cpopup('Error', 'Unexpected error.')
        threading.Thread(target=change_in_new_thread).start()
        gui.popup('Started', 'Check your email for confirmation')
    except:
        gui.popup('Error', 'Unexpected error.')
