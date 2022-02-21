import json
import requests
import os
import hashlib
import modules.vars as horsy_vars
from rich import print


def add_to_cfg(key):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    config['vt-key'] = key

    with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
        json.dump(config, f)


def get_key():
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    try:
        return config['vt-key']
    except KeyError:
        return None


def scan_file(filename):
    api_url = 'https://www.virustotal.com/api/v3/files'
    headers = {'x-apikey': get_key()}
    with open(filename, 'rb') as file:
        files = {'file': (filename, file)}
        if os.path.getsize(filename) < 33554432:
            response = requests.post(api_url, headers=headers, files=files)
            return response.json()['data']['id']
        else:
            api_url = 'https://www.virustotal.com/api/v3/files/upload_url'
            response = requests.get(api_url, headers=headers)
            response = requests.post(response.json()['data'], headers=headers, files=files)
            return response.json()['data']['id']


def get_report(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    api_url = 'https://www.virustotal.com/api/v3/files/' + hash_md5.hexdigest()
    headers = {'x-apikey': get_key()}
    response = requests.get(api_url, headers=headers)
    analysis = dict()
    try:
        analysis['detect'] = response.json()['data']['attributes']['last_analysis_stats']
    except:
        analysis['detect'] = 'No data'
    try:
        analysis['link'] = 'https://www.virustotal.com/gui/file/' + response.json()['data']['id']
    except:
        analysis['link'] = 'No data'

    return analysis


def scan_to_cli(filename):
    print(f"Starting virustotal scan")
    if not get_key():
        print(f"[red]Virustotal api key not found[/]")
        print(f"You can add it by entering [bold]horsy --vt \[your key][/] in terminal")
    else:
        print(f"[green]Virustotal api key found[/]")
        print(f"[italic white]If you want to disable scan, type [/][bold]horsy --vt disable[/]"
              f"[italic white] in terminal[/]")
        scan_file(filename)
        print(f"[green]Virustotal scan finished[/]")
        analysis = get_report(filename)
        print(f"[green]You can see report by opening: [white]{analysis['link']}[/]")
        print(f"{analysis['detect']['malicious']} antivirus flagged this file as malicious")

    print(f"[green][OK] Done[/]")
    return analysis
