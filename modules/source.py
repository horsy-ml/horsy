from modules.core.request import request
import json
import webbrowser
import modules.core.vars as horsy_vars
from rich import print
from modules.core.http_status import handle
from ui.modules.popup import popup


def get_source(package, is_gui=False):
    r = request.get(f"{horsy_vars.url}/packages/json/{package}")
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
        if is_gui:
            popup("Error", "No source code available for this app")
        return "No source code available for this app"
