import os
import sys
import math
import threading
import webbrowser
import modules.vars as horsy_vars
from modules.request import request
from PyQt5 import QtWidgets
import ctypes
import modules.gui as gui
import subprocess


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

UiPackageWindow = QtWidgets.QMainWindow()
package_ui = gui.Ui_PackageWindow()
package_ui.setupUi(UiPackageWindow)

if __name__ == "__main__":
    UiMainWindow.show()
    from modules.login import loginload
    ui.username_box.setText(loginload())


# Connected functions
def refresh_gui():
    installed_apps()


def fill_installed(apps: list):
    ui.installed_table.clear()
    ui.installed_table.setColumnCount(4)
    ui.installed_table.setRowCount(math.ceil(len(apps) / 4))
    for i in range(len(apps)):
        ui.installed_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(apps[i])))


def installed_apps():
    from modules.manager import apps_list
    fill_installed(apps_list(True))


def update_app():
    try:
        app_name = ui.installed_table.currentItem().text().replace('!', '')
        if app_name == "":
            return
        else:
            from modules.gui_manager import install
            ui.installed_table.currentItem().setText(app_name)
            install(app_name)
    except:
        return


def uninstall_app():
    try:
        app_name = ui.installed_table.currentItem().text().replace('!', '')
        if app_name == "":
            return
        else:
            from modules.gui_manager import uninstall
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


def check_updates():
    from modules.updates import check
    needupdate = check(True)
    try:
        fill_installed(needupdate)
    except:
        gui.cpopup("Error", str(needupdate))


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
    gui.popup('Upload', str(upload(True, ui)))


def change_password_gui():
    from modules.change_password import change
    change(ui.oldpass_box.toPlainText(), ui.newpass_box.toPlainText())


def change_email_gui():
    from modules.change_email import change
    change(ui.email_box.toPlainText())


def login_logout_gui():
    from modules.login import login
    ui.username_box.setText(login())


def get_users_apps():
    def get_threaded():
        try:
            apps = request.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/users/public"
                               f"/{ui.username_box.text()}").json()
        except:
            print("Error getting user apps")
        try:
            apps = apps['packages']
            ui.manage_packages_table.clear()
            ui.manage_packages_table.setColumnCount(4)
            ui.manage_packages_table.setRowCount(math.ceil(len(apps) / 4))
            for i in range(len(apps)):
                ui.manage_packages_table.setItem(i // 4, i % 4, QtWidgets.QTableWidgetItem(str(apps[i])))
        except:
            print("Error getting user apps")
    threading.Thread(target=get_threaded).start()


def gui_package_edit():
    from modules.package_edit import edit
    try:
        app_name = ui.manage_packages_table.currentItem().text()
        if app_name == "":
            return
        else:
            UiPackageWindow.show()
            edit(app_name, UiPackageWindow)
    except:
        return


def gui_push_version():
    from modules.package_edit import push_version
    try:
        app_name = ui.manage_packages_table.currentItem().text()
        if app_name == "":
            return
        else:
            push_version(app_name)
    except:
        return


# Run functions on startup
if __name__ == "__main__":
    # Checking directories and files
    if not os.path.exists(horsy_vars.horsypath + 'apps'):
        os.makedirs(horsy_vars.horsypath + 'apps')
    if not os.path.isfile(horsy_vars.horsypath + 'config.cfg'):
        with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
            f.write('{}')
    if not os.path.isfile(horsy_vars.horsypath + 'apps/versions.json'):
        with open(horsy_vars.horsypath + 'apps/versions.json', 'w+') as f:
            f.write('{}')
    if os.path.isfile(horsy_vars.horsypath + 'horsygui.old'):
        os.remove(horsy_vars.horsypath + 'horsygui.old')
        gui.popup('Success', 'Removed old horsygui')

    # Checking version
    try:
        f = open(horsy_vars.horsypath + 'apps/version', 'r')
    except:
        gui.popup('Error', 'Horsy may be not installed correctly. Please reinstall it or stop another instances if '
                           'running. If you installed it just now, please restart PC.')
    version = int(f.read())
    if int(request.get('https://github.com/horsy-ml/horsy/raw/master/web_vars/version').text) > version:
        gui.popup('Update', 'New version available! \nWe appreciate your safety, so you need to update horsy.'
                            '\nPress OK and updater will download the latest version.\n'
                            'If you see this message again, or horsy doesn\'t launch, \n'
                            'download updater manually from GitHub.\n\n'
                            'Window will hide while updating.')
        try:
            import urllib.request
            UiMainWindow.close()
            os.rename(horsy_vars.horsypath + "horsygui.exe", horsy_vars.horsypath + "horsygui.old")
            with open(os.path.join(horsy_vars.horsypath) + 'horsygui.exe', 'wb') as f:
                f.write(request.get('https://github.com/horsy-ml/horsy/raw/master/bin/horsygui.exe').content)
            with open(os.path.join(horsy_vars.horsypath) + 'horsy.exe', 'wb') as f:
                f.write(request.get('https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe').content)
            urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                                       horsy_vars.horsypath + '/apps/version')
        except:
            gui.popup('Error', 'Could not download horsy. \nMaybe installation folder is not writable '
                               '(only for admins).\n Please reinstall horsy or update it manually. \n'
                               'Click OK, download file that will be opened in browser copy it to horsy \n'
                               'folder and launch it.\n'
                               'Afterwards, delete updater file and launch horsy again.')
            webbrowser.open('https://github.com/horsy-ml/horsy/raw/master/bin/horsy_updater.exe')

        subprocess.Popen(str(horsy_vars.horsypath + 'horsygui.exe'), shell=True, close_fds=True)
        sys.exit(0)

    get_users_apps()
    installed_apps()

    # Binds
    ui.tabWidget.currentChanged.connect(refresh_gui)
    ui.update_button.clicked.connect(update_app)
    ui.delete_button.clicked.connect(uninstall_app)
    ui.check_updates_button.clicked.connect(check_updates)
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
    ui.changepass_button.clicked.connect(change_password_gui)
    ui.changeemail_button.clicked.connect(change_email_gui)
    ui.loginlogout_button.clicked.connect(login_logout_gui)
    ui.manage_packages_table.itemDoubleClicked.connect(gui_package_edit)
    ui.editowned_button.clicked.connect(gui_package_edit)
    ui.requestupdate_button.clicked.connect(gui_push_version)

    # Handle GUI exiting to exit whole program
    sys.exit(app.exec_())
