import json
import threading
from rich import print
import requests
import modules.vars as horsy_vars
import os
import zipfile
from modules.virustotal import scan_to_cli
from modules.http_status import handle
from modules.download import dl


def install(package):
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}")
    r_code = handle(r.status_code)
    r = r.text
    r = json.loads(r)

    if r_code[1] not in [403, 401]:
        return r_code[1]

    try:
        print(f"[green]App {r['name']} found, information loaded[/]")

        if not os.path.exists('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath)):
            os.makedirs('{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

        print(f"Downloading {r['url'].split('/')[-1]}")
        to_download = [r['url']]
        if r['download']:
            print(f"Found dependency")
            print(f"Downloading {r['download'].split('/')[-1]}")
            to_download.append(r['download'])

        dl(to_download, '{0}apps/{1}'.format(horsy_vars.horsypath, r['name']))
        scan_to_cli('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath))

        def unzip(file, where):
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(where)
                print(f"[green]Extracted[/]")

        if r['url'].split('.')[-1] == 'zip':
            print(f"Extracting {r['url'].split('/')[-1]}")
            unzip('{2}apps/{0}/{1}'.format(r['name'], r['url'].split('/')[-1], horsy_vars.horsypath),
                  '{1}apps/{0}'.format(r['name'], horsy_vars.horsypath))

        if r['download']:
            if scan_to_cli('{2}apps/{0}/{1}'.format(r['name'], r['download'].split('/')[-1],
                                                    horsy_vars.horsypath))['detect']['malicious'] > 0:
                print(f"[red]Dependency can be malicious. It may run now, if this added to installation "
                      f"config[/]")
                input("Press enter if you want continue, or ctrl+c to exit")

        if r['install']:
            print(f"Found install option")
            threading.Thread(target=os.system, args=('{2}apps/{0}/{1}'.format(r['name'], r['install'],
                                                                              horsy_vars.horsypath),)).start()

        # Launch script
        print(f"Generating launch script")

        with open('{1}apps/{0}.bat'.format(r['name'], horsy_vars.horsypath), 'w') as f:
            f.write(f"@ECHO off\n")
            f.write(f"%horsypath:~0,1%:\n")
            f.write(f"cd %horsypath%/apps/{r['name']}\n")
            f.write(f"{r['run']} %*\n")

        # Done message
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
