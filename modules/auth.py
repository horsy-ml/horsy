import json
import sys
import modules.core.vars as horsy_vars
import ctypes


def get_auth(is_gui=False, login_ui=None, Ui_LoginWindow=None):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    try:
        if config['auth']:
            return config['auth']
        else:
            raise Exception('No auth found')
    except:
        if not is_gui:
            print('[!] No auth found, please login first')
            print('email')
            email = input('> ')
            print('password')
            password = input('> ')
            config['auth'] = {'email': email, 'password': password}
            with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
                json.dump(config, f)
            print('[OK] Auth created')
            return config['auth']
        else:
            login_ui.setupUi(Ui_LoginWindow)
            Ui_LoginWindow.show()

            def load_login_now():
                return get_gui_auth(login_ui, Ui_LoginWindow)
            login_ui.login_button.clicked.connect(load_login_now)


def get_auth_without_login():
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    try:
        if config['auth']:
            return config['auth']
        else:
            raise Exception('No auth found')
    except:
        ctypes.windll.user32.MessageBoxW(0, "Login not found. Please, use the login button on account tab. "
                                            "horsy will close now, but you don't need to restart it later",
                                         "No auth", 0)
        sys.exit(0)


def get_gui_auth(login_ui, Ui_LoginWindow):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)
    if login_ui.email_box.text() != '' and login_ui.password_box.text() != '':
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            config['auth'] = {'email': login_ui.email_box.text(), 'password': login_ui.password_box.text()}
            json.dump(config, f)
        Ui_LoginWindow.close()
        ctypes.windll.user32.MessageBoxW(0, "Login updated. To see it, restart horsygui",
                                            "Reload to take effect", 0)


def del_auth():
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    if config['auth']:
        config['auth'] = None
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            json.dump(config, f)

        print('[OK] Auth deleted')
