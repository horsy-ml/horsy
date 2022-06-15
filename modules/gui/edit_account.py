from ui.gui import Ui_MainWindow
from ezzthread import threaded
import json
from modules.core.request import request
from modules.auth import del_auth, get_auth_without_login, save_auth
import modules.core.vars as horsy_vars
from modules.core.http_status import handle
from ui.modules.popup import popup


@threaded
def edit_email(ui: Ui_MainWindow) -> None:
    if ui.change_email_box.text() == "":
        return
    popup("Changing email", "Check your email for confirmation")
    r = request.put(horsy_vars.url + '/users', json={
        'auth': get_auth_without_login(),
        'email': ui.change_email_box.text()
    })
    r_code = handle(r.status_code)
    r = r.text
    try:
        r = json.loads(r)
    except json.decoder.JSONDecodeError:
        r = {'message': 'Server did not return a valid JSON response'}

    if r_code[1] in [403, 401]:
        popup('Editing email', 'Invalid credentials')
        del_auth()
        return

    elif r_code[1] in [200, 201]:
        popup('Editing email', 'Success')
        save_auth(email=ui.change_email_box.text())
        return

    popup('Editing email', f'{r_code[0]}: {r.get("message")}')


@threaded
def edit_password(ui: Ui_MainWindow) -> None:
    if '' in [ui.old_password_box.text(), ui.new_password_box.text()]:
        return

    if ui.old_password_box.text() != get_auth_without_login()['password']:
        popup('Editing password', 'Old password does not match with password in config.cfg')
        return

    r = request.put(horsy_vars.url + '/users', json={
        'auth': get_auth_without_login(),
        'password': ui.new_password_box.text()
    })
    r_code = handle(r.status_code)
    r = r.text
    try:
        r = json.loads(r)
    except json.decoder.JSONDecodeError:
        r = {'message': 'Server did not return a valid JSON response'}

    if r_code[1] in [403, 401]:
        popup('Editing password', 'Invalid credentials')
        del_auth()
        return

    elif r_code[1] in [200, 201]:
        popup('Editing password', 'Success')
        save_auth(password=ui.new_password_box.text())
        return

    popup('Editing password', f'{r_code[0]}: {r.get("message")}')
