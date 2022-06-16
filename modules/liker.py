from modules.core.request import request
import modules.core.vars as horsy_vars
from modules.auth import get_auth
from ui.modules.popup import popup


def like(package, ui=None):
    return send(package, 1, ui)


def dislike(package, ui=None):
    return send(package, 0, ui)


def send(package, type_, ui=None):
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
