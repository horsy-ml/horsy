import json
import hashlib
import modules.core.vars as horsy_vars
from rich import print
import vt


def add_to_cfg(key):
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    config['vt-key'] = key

    with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
        json.dump(config, f)


def get_key():
    with open(horsy_vars.horsypath + 'config.cfg') as f:
        config = json.load(f)

    return dict(config).get('vt-key')


def scan_file(filename):
    client = vt.Client(get_key())

    with open(filename, 'rb') as file:
        return client.scan_file(file, wait_for_completion=True)


def get_report(filename) -> dict[str, dict[str, int], dict[str, str]]:
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    client = vt.Client(get_key())

    file = client.get_object("/files/" + hash_md5.hexdigest())

    analysis = dict()
    try:
        analysis['detect'] = file.last_analysis_stats
    except:
        analysis['detect'] = 'No data'
        raise
    try:
        analysis['link'] = 'https://www.virustotal.com/gui/file/' + file.id
    except:
        analysis['link'] = 'No data'
        raise

    return analysis


def scan_to_cli(filename: str) -> dict[str, dict[str, int], dict[str, str]]:
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

        return analysis
