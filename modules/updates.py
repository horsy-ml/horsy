import json
from modules.core.request import request
import modules.core.vars as horsy_vars
from modules.core.http_status import handle
from modules.cli.manager import apps_list
from rich import print


def check(gui=False):
    r = request.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/"
                    f"{','.join(apps_list(True))}")
    r_code = handle(r.status_code)

    if r_code[1] not in [200, 201]:
        return r_code[0]
    r = r.text
    r = json.loads(r)

    with open(horsy_vars.horsypath + 'apps/versions.json', 'r') as f:
        versions = json.load(f)

    need_update = list()
    for app in r:
        try:
            if versions[app] < r[app]['version']:
                need_update.append(app)
        except (TypeError, KeyError):
            if r[app]['version'] > 0:
                need_update.append(app)
        except Exception as e:
            print(f"[red]Unexpected error![/]")
            print(e)
    need_update.sort()

    if not gui:
        return need_update

    apps = list()
    for app in apps_list(True):
        if app in need_update:
            apps.append("!" + app)
        else:
            apps.append(app)
    return sorted(apps)
