from PyQt5 import QtCore
from ui.gui import Ui_MainWindow
from modules.data.settings import Settings


def open_menu(ui: Ui_MainWindow) -> None:
    """
    Animates the menu to open and close, using animation from config
    :return:
    """
    width = ui.menu.geometry().width()
    Ui_MainWindow.animation = QtCore.QPropertyAnimation(ui.menu, b"minimumWidth")
    Ui_MainWindow.animation.setDuration(Settings.animation()["timing"])
    if width == 64:
        Ui_MainWindow.animation.setStartValue(64)
        Ui_MainWindow.animation.setEndValue(200)
    else:
        Ui_MainWindow.animation.setStartValue(200)
        Ui_MainWindow.animation.setEndValue(64)
    Ui_MainWindow.animation.setEasingCurve(Settings.animation()["animation"])

    Ui_MainWindow.animation.start()


def handle_menu_click(text: str, ui: Ui_MainWindow) -> None:
    """
    Handles the click on the menu and changes the page
    :param text:
    :param ui:
    :return:
    """
    index = {
        "Close menu": [lambda _: open_menu(ui), None],
        "Installed packages": [ui.content.setCurrentIndex, 0],
        "Explore packages": [ui.content.setCurrentIndex, 1],
        "Upload package": [ui.content.setCurrentIndex, 2],
        "Edit packages": [ui.content.setCurrentIndex, 3],
        "Account settings": [ui.content.setCurrentIndex, 4],
        "Settings of GUI": [ui.content.setCurrentIndex, 5]
    }
    index[text][0](index[text][1])
