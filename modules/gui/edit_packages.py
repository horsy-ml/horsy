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
        call(ui.editable_packages_list.addItems, ["Log in first"])
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


@threaded
def fill_package_info(ui: Ui_MainWindow) -> None:
    if ui.editable_packages_list.currentItem().text() in ["Log in first", "No packages"]:
        return

    package = ui.editable_packages_list.currentItem().text()

    r = request.get(f"{horsy_vars.url}/packages/json/{package}")
    handle(r.status_code)
    r = r.text
    r = json.loads(r)
    call(ui.edit_package_name_box.setText, r["name"])
    call(ui.edit_package_desc_box.setText, r["description"])
    call(ui.edit_package_exe_url_box.setText, r["url"])
    call(ui.edit_package_command_box.setText, r["run"])
    call(ui.edit_package_source_box.setText, r["sourceUrl"])
    call(ui.edit_package_dep_url_box.setText, r["download"])
    call(ui.edit_package_dep_run_box.setText, r["install"])

    call(ui.edit_package_form_lay.show)
