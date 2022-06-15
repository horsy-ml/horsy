from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
from modules.updates import check


def check_updates(ui: Ui_MainWindow) -> None:
    call(ui.installed_packages_list.clear)
    call(ui.installed_packages_list.addItems, check(True))
