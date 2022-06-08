import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.gui import Ui_MainWindow
import ui.modules.setup_gui as setup_gui
from ui.modules.menu_handler import handle_menu_click
from modules.data.settings import Settings


settings = Settings.get_settings()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
setup_gui.hide_parts(ui)
MainWindow.show()

ui.menu.itemClicked.connect(lambda: handle_menu_click(ui.menu.currentItem().text(), ui))

sys.exit(app.exec_())
