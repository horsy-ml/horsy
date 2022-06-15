import sys
import threading
from PyQt5 import QtWidgets, QtCore
from ui.gui import Ui_MainWindow
import ui.modules.setup_gui as setup_gui
import modules.gui.manager as manager
from ui.modules.menu_handler import handle_menu_click
from ui.modules.items_expander import (on_installed_click)
from modules.gui.search import (
    search_for_package,
    display_info
)
from modules.source import get_source
from modules.liker import like, dislike
from modules.gui.updates import check_updates
from modules.uploader import upload
from modules.gui.account import log_in, log_out
from modules.data.settings import Settings
from modules.data.check_files import check_files
from modules.gui.settings import save_settings, fill_settings
from modules.gui.edit_packages import (
    fill_users_packages,
    fill_package_info,
    send_edited_package,
    push_version
)
from modules.gui.updater import (
    needs_update,
    update,
    launch_new_horsy
)
from modules.core.exception import hook

sys.excepthook = hook
threading.excepthook = hook

check_files()
settings = Settings.get_settings()


if needs_update():
    from ui.updater import Ui_MainWindow

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    MainWindow.show()
    update(ui)
    ui.launch_button.clicked.connect(lambda: launch_new_horsy())
    ui.exit_button.clicked.connect(lambda: sys.exit(0))
    sys.exit(app.exec_())


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
setup_gui.hide_parts(ui)
MainWindow.show()
setup_gui.fill_apps_list(ui)
setup_gui.fill_account_page(ui)
fill_users_packages(ui)

try:
    fill_settings(ui)
except Exception as e:
    print(e)
    Settings.fix()

ui.menu.itemClicked.connect(lambda: handle_menu_click(ui.menu.currentItem().text(), ui))
ui.installed_packages_list.itemClicked.connect(lambda: on_installed_click(ui))
ui.installed_packages_list.itemDoubleClicked.connect(
    ui.installed_packages_from_list_lay.hide
)
ui.uninstall_package_button.clicked.connect(lambda: manager.uninstall(ui))
ui.search_button.clicked.connect(lambda: search_for_package(ui))
ui.search_box.returnPressed.connect(lambda: search_for_package(ui))
ui.search_packages_list.itemClicked.connect(lambda: display_info(ui))
ui.install_package_button.clicked.connect(lambda: manager.install(ui))
ui.update_package_button.clicked.connect(lambda: manager.install(ui, ui.installed_packages_list.currentItem().text()
                                                                 .replace('!', '')
                                                                 .replace('Install packages on explore page', '')))
ui.get_source_button.clicked.connect(lambda: get_source(ui.search_packages_list.currentItem().text(), True))
ui.like_button.clicked.connect(lambda: like(ui.search_packages_list.currentItem().text(), ui))
ui.dislike_button.clicked.connect(lambda: dislike(ui.search_packages_list.currentItem().text(), ui))
ui.check_updates_button.clicked.connect(lambda: check_updates(ui))
ui.new_package_upload_button.clicked.connect(lambda: upload(ui))
ui.login_button.clicked.connect(lambda: log_in(ui))
ui.logout_button.clicked.connect(lambda: log_out(ui))
ui.editable_packages_list.itemClicked.connect(lambda: fill_package_info(ui))
ui.edit_package_button.clicked.connect(lambda: send_edited_package(ui))
ui.force_upgrade_button.clicked.connect(lambda: push_version(ui))
ui.save_settings_button.clicked.connect(lambda: save_settings(ui))

sys.exit(app.exec_())
