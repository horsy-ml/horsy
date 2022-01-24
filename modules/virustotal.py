import json
import requests
import os
import hashlib
import modules.vars as horsy_vars


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
    analysis['detect'] = response.json()['data']['attributes']['last_analysis_stats']
    analysis['link'] = 'https://www.virustotal.com/gui/file/' + response.json()['data']['id']
    return analysis
