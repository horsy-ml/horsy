import threading
from ui.gui import Ui_MainWindow
from modules.search import info
from qt_thread_updater import get_updater


def on_installed_click_(ui: Ui_MainWindow) -> None:
    ui.installed_packages_from_list_lay.show()
    get_updater().call_latest(ui.installed_package_desc.setText, 'Loading...')
    get_updater().call_latest(ui.installed_package_desc.setText, info(ui.installed_packages_list.currentItem().text()))


def on_installed_click(ui: Ui_MainWindow) -> None:
    threading.Thread(target=on_installed_click_, args=(ui,)).start()
