from modules.auth import get_auth
from horsygui import login_ui, UiLoginWindow as Ui_LoginWindow
import modules.gui as gui
from modules.request import request
import modules.vars as horsy_vars
from modules.http_status import handle
import json


def edit(package, UiPackageWindow):
    package_ui = gui.Ui_PackageWindow()
    package_ui.setupUi(UiPackageWindow)

    r = request.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}")
    try:
        r_code = handle(r.status_code)
        if r_code[1] not in [200, 201]:
            gui.cpopup("Error", r_code[0])
        r = r.text
        r = json.loads(r)
    except:
        return

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

        gui.cpopup("Updating",
                   handle(request.put(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages",
                                      json=body).status_code)[0])

    package_ui.update_button.clicked.connect(send)


def push_version(package):
    gui.cpopup("Pushing version",
               handle(request.post(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/push-version", json={
                   'auth': get_auth(True, login_ui, Ui_LoginWindow),
                   'name': package
               }).status_code)[0])
