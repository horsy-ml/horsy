from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
from modules.core.request import request
import modules.core.vars as horsy_vars
from modules.auth import get_auth_without_login
from modules.auth import get_auth, del_auth
from modules.core.http_status import handle
from ezzthread import threaded
import json
import time


@threaded
def fill_users_packages(ui: Ui_MainWindow) -> None:
    call(ui.editable_packages_list.clear)
    if not get_auth_without_login(True):
        call(ui.editable_packages_list.addItems, ["Log in first"])
        return

    while ui.logged_in_name_box.text() in ["Loading...", ""]:
        time.sleep(1)

    r = request.get(f"{horsy_vars.url}/users/public/{ui.logged_in_name_box.text()}")
    r_code = handle(r.status_code)
    if r_code[1] not in [200, 201]:
        return r_code[0]
    r = r.text
    if r == "{}":
        call(ui.editable_packages_list.addItems, ["No packages"])
        return
    call(ui.editable_packages_list.addItems, json.loads(r)["packages"])


@threaded
def fill_package_info(ui: Ui_MainWindow) -> None:
    if ui.editable_packages_list.currentItem().text() in ["Log in first", "No packages"]:
        return

    package = ui.editable_packages_list.currentItem().text()

    r = request.get(f"{horsy_vars.url}/packages/json/{package}")
    handle(r.status_code)
    r = r.text
    r = json.loads(r)
    call(ui.edit_package_name_box.setText, r["name"])
    call(ui.edit_package_desc_box.setText, r["description"])
    call(ui.edit_package_exe_url_box.setText, r["url"])
    call(ui.edit_package_command_box.setText, r["run"])
    call(ui.edit_package_source_box.setText, r["sourceUrl"])
    call(ui.edit_package_dep_url_box.setText, r["download"])
    call(ui.edit_package_dep_run_box.setText, r["install"])

    call(ui.edit_package_form_lay.show)


def fill_from_edit(ui: Ui_MainWindow):
    from modules.uploader import matches, urlmatch
    auth = get_auth()

    project_name = ui.edit_package_name_box.text()
    if not matches(project_name) or len(project_name) > 64 or len(project_name) < 3:
        call(ui.edit_result_label.show)
        call(ui.edit_result_label.setText, 'Invalid project name')
        return

    description = ui.edit_package_desc_box.toPlainText()
    if len(description) > 256:
        call(ui.edit_result_label.show)
        call(ui.edit_result_label.setText, 'Description is too long')
        return

    url = ui.edit_package_exe_url_box.text()
    if not urlmatch(url):
        call(ui.edit_result_label.show)
        call(ui.edit_result_label.setText, 'Invalid file url')
        return

    download = ui.edit_package_dep_url_box.text()
    if download == '':
        download = None
    elif not urlmatch(download):
        call(ui.edit_result_label.show)
        call(ui.edit_result_label.setText, 'Invalid download url')
        return

    run = ui.edit_package_command_box.text()
    if run == '':
        call(ui.edit_result_label.show)
        call(ui.edit_result_label.setText, 'Please, specify runtime')
        return

    return dict({
            'auth': auth,
            'name': project_name,
            'description': description,
            'url': url,
            'sourceUrl': (lambda x: None if x == '' else x)(ui.edit_package_source_box.text()),
            'download': download,
            'install': (lambda x: None if x == '' else x)(ui.edit_package_dep_run_box.text()),
            'run': run
        })


@threaded
def send_edited_package(ui: Ui_MainWindow) -> None:
    request_body = fill_from_edit(ui)
    if request_body is None:
        return

    call(ui.edit_result_label.show)
    call(ui.edit_result_label.setText, 'Sending...')

    r = request.put(horsy_vars.url + '/packages', json=request_body)
    r_code = handle(r.status_code)
    r = r.text
    try:
        r = json.loads(r)
    except json.decoder.JSONDecodeError:
        r = {"Message": "Server didn't respond with json"}

    if r_code[1] in [403, 401]:
        del_auth()
        get_auth(ui)
        return

    elif r_code[1] in [200, 201]:
        call(ui.edit_result_label.show)
        call(ui.edit_result_label.setText, 'Success, package has been edited')
        return

    call(ui.edit_result_label.show)
    call(ui.edit_result_label.setText, f'{r_code[0]}: {r.get("message")}')


@threaded
def push_version(ui: Ui_MainWindow) -> None:
    if ui.editable_packages_list.currentItem().text() in ["Log in first", "No packages"]:
        return

    package = ui.editable_packages_list.currentItem().text()

    call(ui.edit_result_label.show)
    call(ui.edit_result_label.setText, 'Sending...')

    r = request.post(horsy_vars.url + '/packages/push-version', json={
        'auth': get_auth(),
        'name': package
    })
    r_code = handle(r.status_code)
    r = r.text
    try:
        r = json.loads(r)
    except json.decoder.JSONDecodeError:
        r = {"Message": "Server didn't respond with json"}

    if r_code[1] in [403, 401]:
        del_auth()
        get_auth(ui)
        return

    elif r_code[1] in [200, 201]:
        call(ui.edit_result_label.show)
        call(ui.edit_result_label.setText, 'Success, users will be notified')
        return

    call(ui.edit_result_label.show)
    call(ui.edit_result_label.setText, f'{r_code[0]}: {r.get("message")}')
