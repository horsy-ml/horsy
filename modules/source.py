import requests
import json
import webbrowser
import modules.vars as horsy_vars
from rich import print
from modules.http_status import handle


def get_source(package):
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}")
    r_code = handle(r.status_code)
    if r_code[1] not in [200, 201]:
        return r_code[0]
    r = r.text
    r = json.loads(r)

    try:
        webbrowser.open(r["sourceUrl"])
        return None
    except:
        print("[red]No source code available for this app[/]")
        return "No source code available for this app"
