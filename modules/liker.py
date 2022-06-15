from modules.core.request import request
import modules.core.vars as horsy_vars
from modules.auth import get_auth
from ui.modules.popup import popup
from ui.gui import Ui_MainWindow


def like(package, ui: Ui_MainWindow):
    return send(package, 1, ui)


def dislike(package, ui: Ui_MainWindow):
    return send(package, 0, ui)


def send(package, type_, ui: Ui_MainWindow):
    body = {
        "auth": get_auth(ui),
        "rate": type_,
        "packageName": package
    }
    r = request.post(f"{horsy_vars.url}/packages/rate", json=body).json()
    print(r["message"])
    if ui:
        popup("Rate", r["message"])
    return r["message"]
