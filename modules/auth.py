import json
import modules.vars as horsy_vars


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
            Ui_LoginWindow.show()
            login_ui.login_button.clicked.connect(lambda: get_gui_auth(login_ui=login_ui,
                                                                       Ui_LoginWindow=Ui_LoginWindow))


def get_gui_auth(login_ui, Ui_LoginWindow):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)
    if login_ui.email_box.text() != '' and login_ui.password_box.text() != '':
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            config['auth'] = {'email': login_ui.email_box.text(), 'password': login_ui.password_box.text()}
            json.dump(config, f)
        Ui_LoginWindow.close()


def del_auth():
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)
    if config['auth']:
        config['auth'] = None
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            json.dump(config, f)
        print('[OK] Auth deleted')
