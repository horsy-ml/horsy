from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
from modules.core.request import request


def fill_users_packages(ui: Ui_MainWindow) -> None:
    call(ui.editable_packages_list.clear)
