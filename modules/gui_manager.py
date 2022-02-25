import json
import threading
from modules.http_status import handle
import requests
import modules.vars as horsy_vars
import os
import zipfile
from modules.virustotal import get_key, scan_file, get_report
from horsygui import UiDownloadWindow, download_ui
from modules.gui import cpopup
from PyQt5 import QtGui


def install(package):
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}")
    r_code = handle(r.status_code)
    r = r.text
    r = json.loads(r)

    if r_code[1] not in [200, 201]:
        cpopup("Error", r_code[1])

    try:
        UiDownloadWindow.show()
        download_ui.logs_box.clear()
        download_ui.logs_box.append(f"Downloading {r['url'].split('/')[-1]}")

        def install_this():
            if not os.path.exists('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath)):
                os.makedirs('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

            def dl_main_file():
                global success
                UiDownloadWindow.show()
                file_r = requests.get(r['url'], stream=True)
                chunk_size = int(int(file_r.headers['Content-Length']) / 100)
                percent = 0
                with open('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath), "wb") as f:
                    for chunk in file_r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            percent += 1
                            f.write(chunk)
                download_ui.logs_box.append("")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

            threads = list()
            threads.append(threading.Thread(target=dl_main_file))

            if r['download']:
                download_ui.logs_box.append(f"Downloading {r['download'].split('/')[-1]}")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

                def dl_dep_file():
                    global success
                    file_r = requests.get(r['download'], stream=True)
                    chunk_size = int(int(file_r.headers['Content-Length']) / 100)
                    with open('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1], horsy_vars.horsypath),
                              "wb") as f:
                        for chunk in file_r.iter_content(chunk_size=chunk_size):
                            if chunk:
                                f.write(chunk)
                    download_ui.logs_box.append("")
                    download_ui.logs_box.append(f"Starting virustotal scan for dependency")
                    download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

                threads.append(threading.Thread(target=dl_dep_file))

            for t in threads:
                t.start()

            for t in threads:
                t.join()

            def unzip(file, where):
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(where)
                    download_ui.logs_box.append(f"Extracted")
                    download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

            if r['url'].split('.')[-1] == 'zip':
                download_ui.logs_box.append(f"Extracting {r['url'].split('/')[-1]}")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
                unzip('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath),
                      '{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

            download_ui.logs_box.append("")
            download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

            if not get_key():
                download_ui.logs_box.append("Virustotal api key not found \n"
                                            "You can add it by entering horsy --vt [key] in terminal")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
            else:
                download_ui.logs_box.append("If you want to disable scan, type horsy --vt disable in terminal")
                download_ui.logs_box.append("Starting virustotal scan for program")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
                scan_file('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath))
                analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1],
                                                               horsy_vars.horsypath))
                download_ui.logs_box.append(f"Scan finished for program \nYou can see report for program by opening: "
                                            f"{analysis['link']} \n"
                                    f"{analysis['detect']['malicious']} antivirus flagged this file as malicious")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

                if r['download']:
                    download_ui.logs_box.append("")
                    download_ui.logs_box.append("Starting virustotal scan for dependency")
                    download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
                    scan_file('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1], horsy_vars.horsypath))
                    download_ui.logs_box.append(f"Scan finished for dependency")
                    download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
                    analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1],
                                                                   horsy_vars.horsypath))
                    download_ui.logs_box.append(f"You can see report for dependency by opening: {analysis['link']}")
                    download_ui.logs_box.append(f"{analysis['detect']['malicious']} "
                                                f"antivirus flagged this file as malicious")
                    download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
                    if analysis['detect']['malicious'] > 0:
                        download_ui.logs_box.append("")
                        download_ui.logs_box.append(f"SECURITY WARNING, APP INSTALLATION STOPPED")
                        download_ui.logs_box.append(f"Dependency can be malicious. "
                                                    f"It may run now, if this added to installation config")
                        download_ui.logs_box.append(f"You can disable VT check with horsy --vt disable \n"
                                                    f"or use horsy CLI to force install")
                        download_ui.logs_box.append("")
                        download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

            download_ui.logs_box.append("")
            download_ui.logs_box.append("Generating launch script")
            with open('{1}apps/{0}.bat'.format(r['name'], horsy_vars.horsypath), 'w') as f:
                f.write(f"@ECHO off\n")
                f.write(f"%horsypath:~0,1%:\n")
                f.write(f"cd %horsypath%/apps/{r['name']}\n")
                f.write(f"{r['run']} %*\n")
            download_ui.logs_box.append("")
            download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)

            if r['install']:
                download_ui.logs_box.append(f"Found install option, launching {r['install']}")
                download_ui.logs_box.append("")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
                threading.Thread(target=os.system, args=('{2}apps/{0}/{1}'.format(r['name'], r['install'],
                                                                                  horsy_vars.horsypath),)).start()
                download_ui.logs_box.append(f"All done!\nYou can run your app by entering {r['name']} in terminal")
                download_ui.logs_box.moveCursor(QtGui.QTextCursor.End)
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
