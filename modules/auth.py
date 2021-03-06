import json
import modules.core.vars as horsy_vars
from ui.modules.popup import popup


def get_auth(ui=None):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    if config.get('auth') is not None:
        return config['auth']

    if not ui:
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
        from modules.core.qt_updater import call
        call(ui.content.setCurrentIndex, 6)


def get_auth_without_login(no_popup=False):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    if config.get('auth') is not None:
        return config['auth']

    if not no_popup:
        popup('No auth', "Login not found. Please, log in on account tab.")


def save_gui_auth(ui):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    if ui.login_mail_box.text() != '' and ui.login_password_box.text() != '':
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            config['auth'] = {'email': ui.login_mail_box.text(), 'password': ui.login_password_box.text()}
            json.dump(config, f)


def save_auth(email: str = None, password: str = None):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
        if email:
            config['auth']['email'] = email
        if password:
            config['auth']['password'] = password
        json.dump(config, f)


def del_auth():
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    if config['auth']:
        config['auth'] = None
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            json.dump(config, f)

        print('[OK] Auth deleted')
