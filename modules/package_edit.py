import time
from modules.auth import get_auth
from horsygui import login_ui, UiLoginWindow as Ui_LoginWindow
import modules.gui as gui
import requests
import modules.vars as horsy_vars
import modules.http_status as status
import json


def edit(package, UiPackageWindow):
    package_ui = gui.Ui_PackageWindow()
    package_ui.setupUi(UiPackageWindow)

    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}").text
    if r == "":
        gui.cpopup("Installation", f"Package {package} not found")
        return f"Package {package} not found"
    try:
        r = json.loads(r)
    except:
        print("[red]Error with unsupported message[/]")
        gui.cpopup("Error", "Error with unsupported message")
        return "Error with unsupported message"
    try:
        if r["message"] == "Internal server error":
            print("Internal server error")
            gui.cpopup("Error", "Internal server error")
            return "Internal server error"
        if r["message"] == "Too many requests":
            try:
                if r['message'] == 'Too many requests':
                    while r['message'] == 'Too many requests':
                        time.sleep(0.5)
                        r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}").text
                        try:
                            r = json.loads(r)
                        except:
                            pass
            except:
                pass
    except:
        pass

    package_ui.packagename_box.setText("Editing package " + r["name"])
    package_ui.package_desc_box.setText(r["description"])
    package_ui.url_of_exe_box.setText(r["url"])
    package_ui.source_url_box.setText(r["sourceUrl"])
    package_ui.dependency_url_box.setText(r["download"])
    package_ui.dependency_run_box.setText(r["install"])
    package_ui.main_exe_box.setText(r["run"])

    UiPackageWindow.show()

    def send():
        body = {
            'auth': get_auth(True, login_ui, Ui_LoginWindow),
            'name': package,
            'description': (lambda x: x if x != '' else None)(package_ui.package_desc_box.toPlainText()),
            'url': (lambda x: x if x != '' else None)(package_ui.url_of_exe_box.text()),
            'sourceUrl': (lambda x: x if x != '' else None)(package_ui.source_url_box.text()),
            'download': (lambda x: x if x != '' else None)(package_ui.dependency_url_box.text()),
            'install': (lambda x: x if x != '' else None)(package_ui.dependency_run_box.text()),
            'run': (lambda x: x if x != '' else None)(package_ui.main_exe_box.text())
        }

        r = requests.put(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages", json=body)
        if r.status_code == status.OK:
            gui.cpopup('Success', 'Success, package edited')
        elif r.status_code == status.UNAUTHORIZED:
            gui.cpopup('Error', 'Unauthorized')
        elif r.status_code == status.NOT_FOUND:
            gui.cpopup('Error', 'Package not found or its not yours')
        elif r.status_code == status.BAD_REQUEST:
            gui.cpopup('Error', 'Bad request')
        elif r.status_code == status.INTERNAL_SERVER_ERROR:
            gui.cpopup('Error', 'Internal server error')
        elif r.status_code == status.TOO_MANY_REQUESTS:
            gui.cpopup('Error', 'Too many requests')
        else:
            gui.cpopup('Error', 'Unknown error')

    package_ui.update_button.clicked.connect(send)
