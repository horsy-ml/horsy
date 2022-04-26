import json
import requests
import modules.vars as horsy_vars
from modules.http_status import handle
from modules.manager import apps_list
from rich import print


def check():
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/"
                     f"{','.join(apps_list(True))}")
    r_code = handle(r.status_code)

    if r_code[1] not in [200, 201]:
        return r_code[0]
    r = r.text
    r = json.loads(r)
    print(r)

    update_this = list()

    return update_this
