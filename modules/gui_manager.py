import json
import threading
from modules.http_status import handle
from modules.request import request
import requests
import modules.vars as horsy_vars
import os
import zipfile
from modules.virustotal import get_key, scan_file, get_report
from horsygui import UiDownloadWindow, download_ui
from modules.gui import cpopup
from PyQt5 import QtGui
from urllib.parse import unquote


def log(message):
    download_ui.logs_box.append(message)
    download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)


def install(package):
    r = request.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}")
    r_code = handle(r.status_code)
    r = r.text
    r = json.loads(r)

    if r_code[1] not in [200, 201]:
        cpopup("Error", r_code[0])

    try:
        UiDownloadWindow.show()
        download_ui.logs_box.clear()
        log(f"Downloading {unquote(r['url'].split('/')[-1])}")

        def install_this():
            if not os.path.exists('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath)):
                os.makedirs('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

            def dl_main_file():
                global success
                UiDownloadWindow.show()
                file_r = requests.get(r['url'], stream=True)
                chunk_size = int(int(file_r.headers['Content-Length']) / 100)
                percent = 0
                with open('{2}apps/{0}/{1}'.format(r['name'], unquote(r['url'].split('/')[-1]), horsy_vars.horsypath),
                          "wb") as f:
                    for chunk in file_r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            percent += 1
                            f.write(chunk)
                log("")

            threads = list()
            threads.append(threading.Thread(target=dl_main_file))

            if r['download']:
                log(f"Downloading {unquote(r['download'].split('/')[-1])}")

                def dl_dep_file():
                    global success
                    file_r = requests.get(r['download'], stream=True)
                    chunk_size = int(int(file_r.headers['Content-Length']) / 100)
                    with open('{2}apps/{0}/{1}'.format(r['name'], unquote(r['download'].split('/')[-1]),
                                                       horsy_vars.horsypath), "wb") as f:
                        for chunk in file_r.iter_content(chunk_size=chunk_size):
                            if chunk:
                                f.write(chunk)
                    log("")
                    log(f"Starting virustotal scan for dependency")

                threads.append(threading.Thread(target=dl_dep_file))

            for t in threads:
                t.start()

            for t in threads:
                t.join()

            def unzip(file, where):
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(where)
                    log(f"Extracted")

            if r['url'].split('.')[-1] == 'zip':
                log(f"Extracting {unquote(r['url'].split('/')[-1])}")

                unzip('{2}apps/{0}/{1}'.format(r['name'], unquote(r['url'].split('/')[-1]), horsy_vars.horsypath),
                      '{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

            log("")

            if not get_key():
                log("Virustotal api key not found \n"
                    "You can add it by entering horsy --vt [key] in terminal")

            else:
                try:
                    log("If you want to disable scan, type horsy --vt disable in terminal")
                    log("Starting virustotal scan for program")

                    scan_file('{2}apps/{0}/{1}'.format(r['name'], unquote(r['url'].split('/')[-1]),
                                                       horsy_vars.horsypath))
                    analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], unquote(r['url'].split('/')[-1]),
                                                                   horsy_vars.horsypath))
                    log(f"Scan finished for program \nYou can see report for program by "
                        f"opening: "
                        f"{analysis['link']} \n"
                        f"{analysis['detect']['malicious']} antivirus flagged this file as "
                        f"malicious")

                except:
                    pass

                if r['download']:
                    try:
                        log("")
                        log("Starting virustotal scan for dependency")

                        scan_file('{2}apps/{0}/{1}'.format(r['name'], unquote(r['download'].split('/')[-1]),
                                                           horsy_vars.horsypath))
                        log(f"Scan finished for dependency")

                        analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], unquote(r['download'].split('/')[-1]),
                                                                       horsy_vars.horsypath))
                        log(f"You can see report for dependency by opening: {analysis['link']}")
                        log(f"{analysis['detect']['malicious']} "
                            f"antivirus flagged this file as malicious")

                        if analysis['detect']['malicious'] > 0:
                            log("")
                            log(f"SECURITY WARNING, APP INSTALLATION STOPPED")
                            log(f"Dependency can be malicious. "
                                f"It may run now, if this added to installation config")
                            log(f"You can disable VT check with horsy --vt disable \n"
                                f"or use horsy CLI to force install")
                            log("")

                    except:
                        pass

            if r['url'].split('.')[-1] == 'zip':
                os.remove('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath))

            log("")
            log("Generating launch script")
            with open('{1}apps/{0}.bat'.format(r['name'], horsy_vars.horsypath), 'w') as f:
                f.write(f"@ECHO off\n")
                f.write(f"""{r['run'].replace('$appdir$', f'%horsypath%/apps/{r["name"]}')} %*\n""")
            log("")

            if r['install']:
                log(f"Found install option, launching {r['install']}")
                log("")

                threading.Thread(target=os.system, args=('{2}apps/{0}/{1}'.format(r['name'], r['install'],
                                                                                  horsy_vars.horsypath),)).start()

            # Update versions file
            with open(horsy_vars.horsypath + 'apps/versions.json', 'r') as f:
                versions = json.load(f)
            with open(horsy_vars.horsypath + 'apps/versions.json', 'w') as f:
                versions[r['name']] = r['version']
                f.write(json.dumps(versions))

            log(f"All done!\nYou can run your app by entering {r['name']} in terminal")

        threading.Thread(target=install_this).start()

    except:
        pass


def uninstall(package):
    if os.path.exists('{1}apps/{0}'.format(package, horsy_vars.horsypath)):
        os.system('rmdir /s /q "{1}apps/{0}"'.format(package, horsy_vars.horsypath))
        cpopup("Uninstallation", f"Files deleted")
    else:
        cpopup("Uninstallation", f"App {package} is not installed or doesn't have files")
    if os.path.isfile('{1}apps/{0}.bat'.format(package, horsy_vars.horsypath)):
        os.remove("{1}apps/{0}.bat".format(package, horsy_vars.horsypath))
        cpopup("Uninstallation", f"Launch script deleted")
    else:
        cpopup("Uninstallation", f"App {package} is not installed or doesn't have launch script")
