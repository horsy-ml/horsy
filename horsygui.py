import sys
import math
import webbrowser
import modules.vars as horsy_vars
from PyQt5 import QtWidgets
import ctypes
import modules.gui as gui


# Hide console window (does not work on custom terminals like Windows Terminal)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Initialize GUI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

UiMainWindow = QtWidgets.QMainWindow()
ui = gui.Ui_MainWindow()
ui.setupUi(UiMainWindow)

UiLoginWindow = QtWidgets.QMainWindow()
login_ui = gui.Ui_LoginWindow()
login_ui.setupUi(UiLoginWindow)

UiDownloadWindow = QtWidgets.QMainWindow()
download_ui = gui.Ui_DownloadWindow()
download_ui.setupUi(UiDownloadWindow)

if __name__ == "__main__":
    UiMainWindow.show()


# Functions
def refresh_gui():
    installed_apps()


def installed_apps():
    from modules.manager import apps_list
    ui.installed_table.clear()
    apps = apps_list(True)
    ui.installed_table.setColumnCount(4)
    ui.installed_table.setRowCount(math.ceil(len(apps) / 4))
    for i in range(len(apps)):
        ui.installed_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(apps[i])))


def update_app():
    try:
        app_name = ui.installed_table.currentItem().text()
        if app_name == "":
            return
        else:
            from modules.gui_manager import install
            install(app_name)
    except:
        return


def uninstall_app():
    try:
        app_name = ui.installed_table.currentItem().text()
        if app_name == "":
            return
        else:
            from modules.manager import uninstall
            uninstall(app_name)
            installed_apps()
    except:
        return


def search_gui():
    from modules.search import search
    search_query = ui.search_box.toPlainText()
    if search_query == "":
        return
    else:
        found = search(search_query, True)
        ui.search_table.clear()
        ui.search_table.setColumnCount(4)
        ui.search_table.setRowCount(math.ceil(len(found) / 4))
        for i in range(len(found)):
            ui.search_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(found[i])))


def install_app():
    from modules.gui_manager import install
    try:
        app_name = ui.search_table.currentItem().text()
        if app_name == "":
            return
        else:
            install(app_name)
    except:
        return


def get_source_gui():
    from modules.source import get_source
    try:
        app_name = ui.search_table.currentItem().text()
        if app_name == "":
            return
        else:
            source = get_source(app_name)
            if source is not None:
                gui.popup("Error", source)
    except:
        return


def info_gui():
    from modules.search import info
    try:
        app_name = ui.search_table.currentItem().text()
        if app_name == "":
            return
        else:
            info = info(app_name, download_ui, UiDownloadWindow)
            if info is not None:
                gui.popup("Error", info)
    except:
        return


def like_gui():
    from modules.liker import like
    try:
        app_name = ui.search_table.currentItem().text()
        if app_name == "":
            return
        else:
            like = like(app_name, login_ui, UiLoginWindow)
            if 'Success' not in like:
                gui.popup("Like", like)
    except:
        return


def dislike_gui():
    from modules.liker import dislike
    try:
        app_name = ui.search_table.currentItem().text()
        if app_name == "":
            return
        else:
            dislike = dislike(app_name, login_ui, UiLoginWindow)
            if 'Success' not in dislike:
                gui.popup("Dislike", dislike)
    except:
        return


def upload_gui():
    from modules.uploader import upload
    gui.popup('Upload', str(upload(True, ui, login_ui, UiMainWindow)))


# Run functions on startup
if __name__ == "__main__":
    installed_apps()

    # Binds
    ui.tabWidget.currentChanged.connect(refresh_gui)
    ui.update_button.clicked.connect(update_app)
    ui.delete_button.clicked.connect(uninstall_app)
    ui.search_button.clicked.connect(search_gui)
    ui.install_button.clicked.connect(install_app)
    ui.source_button.clicked.connect(get_source_gui)
    ui.info_button.clicked.connect(info_gui)
    ui.search_table.itemDoubleClicked.connect(info_gui)
    ui.like_button.clicked.connect(like_gui)
    ui.dislike_button.clicked.connect(dislike_gui)
    ui.upload_button.clicked.connect(upload_gui)
    ui.regmessage_button.clicked.connect(lambda: webbrowser.open(f"{horsy_vars.protocol}{horsy_vars.server_url}"
                                                                 f"/registration"))

    # Handle GUI exiting to exit whole program
    sys.exit(app.exec_())
