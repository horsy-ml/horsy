from ui.gui import Ui_MainWindow
from modules.cli.manager import apps_list
from ezzthread import threaded
from modules.core.qt_updater import call


def hide_parts(ui: Ui_MainWindow) -> None:
    ui.installed_packages_from_list_lay.hide()
    ui.downloading_dependency_progress.hide()
    ui.downloading_main_file_progress.hide()
    ui.installation_progress.hide()
    ui.search_packages_from_list_lay.hide()
    ui.upload_result_label.hide()
    ui.edit_result_label.hide()
    ui.edit_package_form_lay.hide()
    ui.new_login_lay.hide()
    ui.login_lay.hide()
    ui.change_password_lay.hide()
    ui.change_email_lay.hide()


@threaded
def fill_apps_list(ui: Ui_MainWindow) -> None:
    call(ui.installed_packages_list.clear)
    call(ui.installed_packages_list.addItems, (lambda x: x if x != [] else ['Install packages on explore page'])(
        apps_list(is_gui=True)))


@threaded
def fill_user_apps(ui: Ui_MainWindow) -> None:
    call(ui.editable_packages_list.clear)


@threaded
def fill_account_page(ui: Ui_MainWindow) -> None:
    from modules.auth import get_auth_without_login
    if not get_auth_without_login(True):
        call(ui.new_login_lay.show)
        call(ui.account_settings_vert_spacer_widget.hide)
