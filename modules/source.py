import requests
import json
import webbrowser
import modules.vars as horsy_vars
from rich import print


def get_source(package):
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}").text
    try:
        r = json.loads(r)
    except:
        print("[red]Error with unsupported message[/]")
        return
    try:
        if r["message"] == "not found":
            print("[red]Package not found[/]")
            return
        if r["message"] == "Internal server error":
            print("[red]Internal server error[/]")
            return
    except:
        pass

    try:
        webbrowser.open(r["sourceUrl"])
    except:
        print("[red]No source code available for this app[/]")
