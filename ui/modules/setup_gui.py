from ui.gui import Ui_MainWindow
from modules.cli.manager import apps_list


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


def fill_existing_data(ui: Ui_MainWindow) -> None:
    ui.installed_packages_list.clear()
    ui.installed_packages_list.addItems(apps_list(is_gui=True))
