from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
from ezzthread import threaded
import modules.core.vars as horsy_vars
from ui.modules.setup_gui import fill_apps_list
from modules.core.request import request
from modules.core.http_status import handle
from modules.gui.virustotal import scan_to_gui
from modules.gui.downloader import dl
from modules.gui.updates import check_updates
import os
import json
import zipfile
import threading


@threaded
def install(ui: Ui_MainWindow, package: str = None) -> None:
    if package == '':
        return
    package = ui.search_packages_list.currentItem().text() if not package else package
    call(ui.search_packages_from_list_lay.show)
    call(ui.update_package_button.setEnabled, False)
    call(ui.search_results.hide)
    call(ui.search_bar_lay.hide)
    call(ui.search_buttons_lay.hide)
    call(ui.search_package_desc.clear)
    call(ui.installation_progress.show)
    call(ui.installation_progress.setValue, 0)
    call(ui.installation_progress.setMaximum, 10)
    call(ui.installed_package_desc.setText, f'App {package} is being installed, check progress on explore page.')

    r = request.get(f"{horsy_vars.url}/packages/json/{package}")
    r_code = handle(r.status_code)
    r = r.text
    try:
        r = json.loads(r)
    except json.decoder.JSONDecodeError:
        call(ui.search_package_desc.append, f"App {package} not found or server can't handle your request")
        return

    if r_code[1] not in [200, 201]:
        return r_code[0]

    # Inform the user
    call(ui.search_package_desc.append, f"App {r['name']} found, information loaded")
    call(ui.installation_progress.setValue, 1)

    # Create the app directory
    if not os.path.exists('{1}apps\{0}'.format(r['name'], horsy_vars.horsypath)):
        os.makedirs('{1}apps\{0}'.format(r['name'], horsy_vars.horsypath))
    call(ui.installation_progress.setValue, 2)

    # Download all files
    dl(ui, r['url'], '{0}apps\{1}'.format(horsy_vars.horsypath, r['name']), r['download'])
    call(ui.installation_progress.setValue, 3)

    # Scan main file
    scan_to_gui(ui, '{2}apps\{0}\{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath))
    call(ui.search_package_desc.append, "")
    call(ui.installation_progress.setValue, 4)

    # Unzip the main file if needed
    def unzip(file, where):
        with zipfile.ZipFile(file) as zip_ref:
            zip_ref.extractall(where)
            call(ui.search_package_desc.append, f"Extracted")

    if r['url'].split('.')[-1] == 'zip':
        call(ui.search_package_desc.append, f"Extracting {r['url'].split('/')[-1]}")
        unzip('{2}apps\{0}\{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath),
              '{1}apps\{0}'.format(r['name'], horsy_vars.horsypath))
        os.remove('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath))
        call(ui.search_package_desc.append, "")
    call(ui.installation_progress.setValue, 5)

    # Scan dependencies
    try:
        if r['download'] and scan_to_gui(ui,
                                         '{2}apps\{0}\{1}'.format(r['name'], r['download'].split('/')[-1],
                                                                  horsy_vars.horsypath)
                                         )['detect']['malicious'] > 0:
            call(ui.search_package_desc.append, "Dependency can be malicious. It may run now, if this added to "
                                                "installation config. Install it manually (with CLI)")
            return
    except TypeError:
        pass
    call(ui.installation_progress.setValue, 6)

    # Execute install script
    if r['install']:
        call(ui.search_package_desc.append, f"Found install option")
        threading.Thread(target=os.system, args=('{2}apps\{0}\{1}'.format(r['name'], r['install'],
                                                                          horsy_vars.horsypath),)).start()
        call(ui.search_package_desc.append, "")
    call(ui.installation_progress.setValue, 7)

    # Create launch script
    call(ui.search_package_desc.append, f"Generating launch script")

    with open('{1}apps\{0}.bat'.format(r['name'], horsy_vars.horsypath), 'w+') as f:
        f.write(f"@ECHO off\n")
        f.write(f"""{r['run'].replace('$appdir$', f'%horsypath%/apps/{r["name"]}')} %*\n""")
    call(ui.installation_progress.setValue, 8)

    # Update versions file
    with open(horsy_vars.horsypath + 'apps/versions.json', 'r') as f:
        versions = json.load(f)
    with open(horsy_vars.horsypath + 'apps/versions.json', 'w') as f:
        versions[r['name']] = r['version']
        f.write(json.dumps(versions))
        call(ui.search_package_desc.append, f"Versions file updated")
    call(ui.installation_progress.setValue, 9)

    # Done message
    call(ui.search_package_desc.append, f"All done!")
    call(ui.search_package_desc.append,
         f"You can run your app by entering {r['name']} in terminal")
    call(ui.installation_progress.setValue, 10)

    call(ui.update_package_button.setEnabled, True)
    call(ui.search_results.show)
    call(ui.search_bar_lay.show)
    call(ui.search_buttons_lay.show)
    call(ui.installation_progress.hide)
    call(ui.downloading_main_file_progress.hide)
    call(ui.downloading_dependency_progress.hide)
    call(ui.installed_package_desc.append, f'Successfully installed {package}')
    check_updates(ui)

@threaded
def uninstall(ui: Ui_MainWindow) -> None:
    """
    Uninstall package
    :param package:
    :param ui:
    :return:
    """
    package = ui.installed_packages_list.currentItem().text().replace('!', '')
    call(ui.installed_package_desc.clear)
    call(ui.installed_package_desc.setText, f'Uninstalling {package}...')
    if os.path.exists('{1}apps/{0}'.format(package, horsy_vars.horsypath)):
        os.system('rmdir /s /q "{1}apps/{0}"'.format(package, horsy_vars.horsypath))
        call(ui.installed_package_desc.append, "Files deleted")
    else:
        call(ui.installed_package_desc.append, f"App {package} is not installed or doesn't have files")
    if os.path.isfile('{1}apps/{0}.bat'.format(package, horsy_vars.horsypath)):
        os.remove("{1}apps/{0}.bat".format(package, horsy_vars.horsypath))
        call(ui.installed_package_desc.append, f"Launch script deleted")
    else:
        call(ui.installed_package_desc.append, f"App {package} is not installed or doesn't have launch script")
    fill_apps_list(ui)
    call(ui.installed_package_desc.append, f"Done!")
