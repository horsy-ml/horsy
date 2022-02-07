import json
import threading
from rich import print
import requests
import modules.vars as horsy_vars
from tqdm import tqdm
import os
import zipfile
from modules.virustotal import get_key, scan_file, get_report


def install(package):
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}").text
    if r == "":
        print(f"[red]Package {package} not found[/]")
        return
    try:
        r = json.loads(r)
    except:
        print("[red]Error with unsupported message[/]")
        return
    try:
        if r["message"] == "Internal server error":
            print("[red]Internal server error[/]")
            return
    except:
        pass

    try:
        print(f"[green]App {r['name']} found, information loaded[/]")

        if not os.path.exists('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath)):
            os.makedirs('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

        # if not is_gui:
        print(f"Downloading {r['url'].split('/')[-1]}")

        chunk_size = 1024
        file_r = requests.get(r['url'], stream=True)
        with open('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath), "wb") as f:
            pbar = tqdm(unit="B", unit_scale=True, total=int(file_r.headers['Content-Length']))
            for chunk in file_r.iter_content(chunk_size=chunk_size):
                if chunk:
                    pbar.update(len(chunk))
                    f.write(chunk)
            pbar.close()

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

            chunk_size = 1024
            file_r = requests.get(r['download'], stream=True)
            with open('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1], horsy_vars.horsypath),
                      "wb") as f:
                pbar = tqdm(unit="B", unit_scale=True, total=int(file_r.headers['Content-Length']))
                for chunk in file_r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        pbar.update(len(chunk))
                        f.write(chunk)
                pbar.close()

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
            f.write(f"%horsypath:~0,1%:\n")
            f.write(f"cd %horsypath%/apps/{r['name']}\n")
            f.write(f"{r['run']} %*\n")

        print(f"[green][OK] All done![/]")
        print(f"[green]You can run your app by entering [italic white]{r['name']}[/] in terminal[/]")

    except:
        print("[red]Unexpected error[/]")
        # raise
        return


def uninstall(package):
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


def apps_list(is_gui=False):
    apps = list()
    if os.path.exists('{0}apps'.format(horsy_vars.horsypath)):
        if not is_gui:
            print(f"[green]Installed apps:[/]")
        for file in os.listdir('{0}apps'.format(horsy_vars.horsypath)):
            if file.endswith(".bat") and not is_gui:
                print(f"{file.split('.')[0]}")
            elif file.endswith(".bat"):
                apps.append(file.split('.')[0])
    if is_gui:
        return apps
