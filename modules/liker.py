from modules.core.request import request
import modules.core.vars as horsy_vars
from modules.auth import get_auth
from ui.modules.popup import popup


def like(package, is_gui=False, login_ui=None, Ui_LoginWindow=None):
    return send(package, 1, is_gui, login_ui, Ui_LoginWindow)


def dislike(package, is_gui=False, login_ui=None, Ui_LoginWindow=None):
    return send(package, 0, is_gui, login_ui, Ui_LoginWindow)


def send(package, type_, is_gui=False, login_ui=None, Ui_LoginWindow=None):
    body = {
        "auth": get_auth(is_gui, login_ui, Ui_LoginWindow),
        "rate": type_,
        "packageName": package
    }
    r = request.post(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/rate", json=body).json()
    print(r["message"])
    if is_gui:
        popup("Rate", r["message"])
    return r["message"]
