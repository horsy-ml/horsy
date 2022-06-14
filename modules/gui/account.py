from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
import json
from ezzthread import threaded
from modules.auth import (
    save_gui_auth,
    get_auth_without_login,
    del_auth
)
from modules.core.request import request
from modules.core.http_status import handle
import modules.core.vars as horsy_vars
from ui.modules.popup import popup
from ui.modules.setup_gui import fill_account_page


@threaded
def log_in(ui: Ui_MainWindow):
    save_gui_auth(ui)
    setting_name = set_name(ui)
    if setting_name is not None:
        popup('Error', setting_name)


@threaded
def log_out(ui: Ui_MainWindow):
    del_auth()
    fill_account_page(ui)


def set_name(ui: Ui_MainWindow):
    if get_auth_without_login(True):
        call(ui.new_login_lay.hide)
        call(ui.logged_in_name_box.setText, "Loading...")
        call(ui.login_lay.show)
        r = request.get(f"{horsy_vars.url}/users/login",
                        json={'auth': get_auth_without_login(True)})
        r_code = handle(r.status_code)
        if r_code[1] not in [200, 201]:
            log_out(ui)
            return r_code[0]
        r = r.text
        r = json.loads(r)
        call(ui.new_login_lay.hide)
        call(ui.logged_in_name_box.setText, r["message"])
        call(ui.login_lay.show)
        call(ui.account_settings_vert_spacer_widget.show)
        call(ui.change_email_lay.show)
        call(ui.change_password_lay.show)
