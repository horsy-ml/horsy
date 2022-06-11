import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.gui import Ui_MainWindow
import ui.modules.setup_gui as setup_gui
from ui.modules.menu_handler import handle_menu_click
from ui.modules.items_expander import (on_installed_click)
from modules.data.settings import Settings


settings = Settings.get_settings()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
setup_gui.hide_parts(ui)
MainWindow.show()
setup_gui.fill_existing_data(ui)

ui.menu.itemClicked.connect(lambda: handle_menu_click(ui.menu.currentItem().text(), ui))
ui.installed_packages_list.itemClicked.connect(lambda: on_installed_click(ui))
ui.installed_packages_list.itemDoubleClicked.connect(
    ui.installed_packages_from_list_lay.hide
)

sys.exit(app.exec_())
