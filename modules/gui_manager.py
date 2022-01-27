import json
import threading
import time
from modules.unerrored import run_threaded, run
import requests
import modules.vars as horsy_vars
import os
import zipfile
from modules.virustotal import get_key, scan_file, get_report
from horsygui import UiDownloadWindow, download_ui
from modules.gui import popup
success = 0


def install(package):
    global success
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}").text
    if r == "":
        run_threaded(popup("Installation", f"Package {package} not found"))
        return f"Package {package} not found"
    try:
        r = json.loads(r)
    except:
        print("[red]Error with unsupported message[/]")
        run_threaded(popup("Error", "Error with unsupported message"))
        return "Error with unsupported message"
    try:
        if r["message"] == "Internal server error":
            print("[red]Internal server error[/]")
            run_threaded(popup("Error", "Internal server error"))
            return "Internal server error"
    except:
        pass

    try:
        UiDownloadWindow.show()

        if not os.path.exists('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath)):
            os.makedirs('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

        download_ui.logs_box.clear()
        download_ui.logs_box.append(f"Downloading {r['url'].split('/')[-1]}")

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
                        # download_ui.progress_box_1.setText(f"{percent}% {'|' * percent}")

            if not get_key():
                download_ui.logs_box.append("Virustotal api key not found \n"
                                            "You can add it by entering horsy --vt in terminal")
            else:
                download_ui.logs_box.append("If you want to disable scan, type horsy --vt disable in terminal")
                scan_file('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath))
                analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1],
                                                               horsy_vars.horsypath))
                download_ui.logs_box.append(f"Scan finished for program \nYou can see report by opening: "
                                            f"{analysis['link']} \n"
                                    f"{analysis['detect']['malicious']} antivirus flagged this file as malicious")

            def unzip(file, where):
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(where)
                    print(f"Extracted")

            if r['url'].split('.')[-1] == 'zip':
                print(f"Extracting {r['url'].split('/')[-1]}")
                unzip('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath),
                      '{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

            success += 1

        threads = list()
        threads.append(threading.Thread(target=dl_main_file))

        if r['download']:
            def dl_dep_file():
                global success
                download_ui.logs_box.append(f"Downloading {r['download'].split('/')[-1]}")
                file_r = requests.get(r['download'], stream=True)
                chunk_size = int(int(file_r.headers['Content-Length']) / 100)
                with open('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1], horsy_vars.horsypath),
                          "wb") as f:
                    for chunk in file_r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)
                download_ui.logs_box.append(f"Starting virustotal scan for dependency")
                if not get_key():
                    download_ui.logs_box.append(f"Virustotal api key not found")
                    download_ui.logs_box.append(f"You can add it by entering horsy --vt in terminal")
                else:
                    scan_file('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1], horsy_vars.horsypath))
                    download_ui.logs_box.append(f"Virustotal scan finished for dependency")
                    analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1],
                                                                   horsy_vars.horsypath))
                    download_ui.logs_box.append(f"You can see report for dependency by opening: {analysis['link']}")
                    download_ui.logs_box.append(f"{analysis['detect']['malicious']} "
                                                f"antivirus flagged this file as malicious")
                    if analysis['detect']['malicious'] > 0:
                        download_ui.logs_box.append(f"Dependency can be malicious. "
                                                    f"It may run now, if this added to installation config")
                        download_ui.logs_box.append(f"You can disable VT check with horsy --vt disable \n"
                                                    f"or use horsy CLI to force install")
                        success -= 1
                        return

                success += 1

            threads.append(threading.Thread(target=dl_dep_file))

        for t in threads:
            t.start()

        with open('{1}apps/{0}.bat'.format(r['name'], horsy_vars.horsypath), 'w') as f:
            f.write(f"@ECHO off\n")
            f.write(f"{horsy_vars.horsypath}apps/{r['name']}/{r['run']} %*\n")

        def wait_for_success():
            while success != 2:
                time.sleep(1)
            if success == 2:
                if r['install']:
                    download_ui.logs_box.append(f"Found install option")
                    threading.Thread(target=os.system, args=('{2}apps/{0}/{1}'.format(r['name'], r['install'],
                                                                                      horsy_vars.horsypath),)).start()
                download_ui.logs_box.append(f"All done!\n You can run your app by entering {r['name']} in terminal")
                return
        threading.Thread(target=wait_for_success).start()

    except:
        pass


def uninstall(package, is_gui=False):
    if os.path.exists('{1}apps/{0}'.format(package, horsy_vars.horsypath)):
        os.system('rmdir /s /q "{1}apps/{0}"'.format(package, horsy_vars.horsypath))
        print(f"[green][OK] Files deleted[/]")
    else:
        print(f"[red]App {package} is not installed or doesn't have files[/]")
    if os.path.isfile('{1}apps/{0}.bat'.format(package, horsy_vars.horsypath)):
        os.remove("{1}apps/{0}.bat".format(package, horsy_vars.horsypath))
        print(f"[green][OK] Launch script deleted[/]")
    else:
        print(f"[red]App {package} is not installed or doesn't have launch script[/]")
