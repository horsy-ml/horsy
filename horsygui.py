import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.gui import Ui_MainWindow
import ui.modules.setup_gui as setup_gui
import modules.gui.manager as manager
from ui.modules.menu_handler import handle_menu_click
from ui.modules.items_expander import (on_installed_click)
from modules.gui.search import (
    search_for_package,
    display_info
)
from modules.data.settings import Settings
from modules.core.exception import hook

sys.excepthook = hook

settings = Settings.get_settings()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
setup_gui.hide_parts(ui)
MainWindow.show()
setup_gui.fill_apps_list(ui)

ui.menu.itemClicked.connect(lambda: handle_menu_click(ui.menu.currentItem().text(), ui))
ui.installed_packages_list.itemClicked.connect(lambda: on_installed_click(ui))
ui.installed_packages_list.itemDoubleClicked.connect(
    ui.installed_packages_from_list_lay.hide
)
ui.uninstall_package_button.clicked.connect(lambda: manager.uninstall(ui))
ui.search_button.clicked.connect(lambda: search_for_package(ui))
ui.search_box.returnPressed.connect(lambda: search_for_package(ui))
ui.search_packages_list.itemClicked.connect(lambda: display_info(ui))
ui.install_package_button.clicked.connect(lambda: manager.install(ui, MainWindow))

sys.exit(app.exec_())
