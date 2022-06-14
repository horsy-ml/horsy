from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
from modules.core.request import request
import modules.core.vars as horsy_vars
from modules.auth import get_auth_without_login
from modules.core.http_status import handle
from ezzthread import threaded
import json
import time


@threaded
def fill_users_packages(ui: Ui_MainWindow) -> None:
    call(ui.editable_packages_list.clear)
    if not get_auth_without_login(True):
        return

    while ui.logged_in_name_box.text() in ["Loading...", ""]:
        time.sleep(1)

    r = request.get(f"{horsy_vars.url}/users/public/{ui.logged_in_name_box.text()}")
    r_code = handle(r.status_code)
    if r_code[1] not in [200, 201]:
        return r_code[0]
    r = r.text
    if r == "{}":
        call(ui.editable_packages_list.addItems, ["No packages"])
        return
    call(ui.editable_packages_list.addItems, json.loads(r)["packages"])
