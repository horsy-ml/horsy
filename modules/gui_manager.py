import json
import threading
import requests
import modules.vars as horsy_vars
import os
import zipfile
from modules.virustotal import get_key, scan_file, get_report
from horsygui import UiDownloadWindow, download_ui


def install(package):
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}").text
    if r == "":
        return f"Package {package} not found"
    try:
        r = json.loads(r)
    except:
        print("[red]Error with unsupported message[/]")
        return "Error with unsupported message"
    try:
        if r["message"] == "Internal server error":
            print("[red]Internal server error[/]")
            return "Internal server error"
    except:
        pass

    try:
        print(f"[green]App {r['name']} found, information loaded[/]")
        UiDownloadWindow.show()

        if not os.path.exists('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath)):
            os.makedirs('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

        download_ui.logs_box.clear()
        download_ui.logs_box.append(f"Downloading {r['url'].split('/')[-1]}")
        success = 0

        def dl_main_file(success):
            UiDownloadWindow.show()
            file_r = requests.get(r['url'], stream=True)
            chunk_size = int(int(file_r.headers['Content-Length']) / 100)
            with open('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath), "wb") as f:
                for chunk in file_r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        download_ui.progressBar_1.setValue(download_ui.progressBar_1.value() + 1)
                        f.write(chunk)
                download_ui.progressBar_1.setValue(0)
                success += 1

        threading.Thread(target=dl_main_file, args=(success,)).start()

        print(f"Starting virustotal scan")
        if not get_key():
            print(f"[red]Virustotal api key not found[/]")
            print(f"You can add it by entering [bold]horsy --vt \[your key][/] in terminal")
        else:
            print(f"[green]Virustotal api key found[/]")
            print(f"[italic white]If you want to disable scan, type [/][bold]horsy --vt disable[/]"
                  f"[italic white] in terminal[/]")
            scan_file('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath))
            print(f"[green]Virustotal scan finished[/]")
            analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1],
                                                           horsy_vars.horsypath))
            print(f"[green]You can see report by opening: [white]{analysis['link']}[/]")
            print(f"{analysis['detect']['malicious']} antivirus flagged this file as malicious")

        print(f"[green][OK] Done[/]")

        def unzip(file, where):
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(where)
                print(f"[green]Extracted[/]")

        if r['url'].split('.')[-1] == 'zip':
            print(f"Extracting {r['url'].split('/')[-1]}")
            unzip('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath),
                  '{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

        if r['download']:
            print(f"Found dependency")
            # if not is_gui:
            print(f"Downloading {r['download'].split('/')[-1]}")

            def dl_dep_file(success):
                download_ui.logs_box.append(f"Downloading {r['download'].split('/')[-1]}")
                file_r = requests.get(r['download'], stream=True)
                chunk_size = int(int(file_r.headers['Content-Length']) / 100)
                with open('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1], horsy_vars.horsypath),
                          "wb") as f:
                    for chunk in file_r.iter_content(chunk_size=chunk_size):
                        if chunk:
                            download_ui.progressBar_2.setValue(download_ui.progressBar_2.value() + 1)
                            f.write(chunk)
                    download_ui.progressBar_2.setValue(0)
                    success += 1

            threading.Thread(target=dl_dep_file, args=(success,)).start()

            print(f"Starting virustotal scan")
            if not get_key():
                print(f"[red]Virustotal api key not found[/]")
                print(f"You can add it by entering [italic white]horsy --vt \[your key][/] in terminal")
            else:
                print(f"[green]Virustotal api key found[/]")
                scan_file('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1], horsy_vars.horsypath))
                print(f"[green]Virustotal scan finished[/]")
                analysis = get_report('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1],
                                                               horsy_vars.horsypath))
                print(f"[green]You can see report by opening: [white]{analysis['link']}[/]")
                print(f"{analysis['detect']['malicious']} antivirus flagged this file as malicious")
                if analysis['detect']['malicious'] > 0:
                    print(f"[red]Dependency can be malicious. It may run now, if this added to installation "
                          f"config[/]")
                    input("Press enter if you want continue, or ctrl+c to exit")

        if r['install']:
            print(f"Found install option")
            threading.Thread(target=os.system, args=('{2}apps/{0}/{1}'.format(r['name'], r['install'],
                                                                              horsy_vars.horsypath),)).start()

        print(f"Generating launch script")

        with open('{1}apps/{0}.bat'.format(r['name'], horsy_vars.horsypath), 'w') as f:
            f.write(f"@ECHO off\n")
            f.write(f"{horsy_vars.horsypath}apps/{r['name']}/{r['run']} %*\n")

        return f"All done!\n You can run your app by entering {r['name']} in terminal"

    except:
        raise
        return "Unexpected error"


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
