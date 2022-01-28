import requests
import modules.vars as horsy_vars
from modules.auth import get_auth


def like(package, is_gui=False, login_ui=None, Ui_LoginWindow=None):
    body = {
        "auth": get_auth(is_gui, login_ui, Ui_LoginWindow),
        "rate": 1,
        "packageName": package
    }
    r = requests.post(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/rate", json=body).text

