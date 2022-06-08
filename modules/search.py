import textwrap
from algoliasearch.search_client import SearchClient
import os
from modules.core.request import request
import requests
import modules.core.vars as horsy_vars
import json
from rich import print
from modules.core.http_status import handle
from ui.gui import Ui_MainWindow

client = SearchClient.create(
    requests.get('https://raw.githubusercontent.com/horsy-ml/horsy/master/web_vars/search_app').json()['APP_ID'],
    requests.get('https://raw.githubusercontent.com/horsy-ml/horsy/master/web_vars/search_app').json()['API_KEY'])
index = client.init_index('packages')


def search(query, is_gui=False):
    res = index.search(query)['hits']
    ret_res = list()
    for i in res:
        if not is_gui:
            print(textwrap.shorten(f"{i['name']} by {i['authorName']} - {i['description']}",
                                   width=os.get_terminal_size().columns))
        else:
            ret_res.append(i['name'])

    return ret_res


def info(package):
    r = request.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}")
    handle(r.status_code)
    r = r.text
    r = json.loads(r)

    print(f"[bold]{r['name']}{'✅' if r['verified'] else ''} by {r['authorName']}[/]")
    print(f"{r['description']}")
    print(f"👍{r['likes']} | 👎{r['dislikes']}")
    if not r['verified']:
        print("This package is not verified by the horsy team. This means that it \n"
              "can be unstable or it can be malware. Most packages have unverified\n"
              "state, but use it at your own risk.")
    else:
        print("This package is [green]verified[/] by the horsy team! \n"
              "Keep in mind, developers can change the code after verification \n"
              "We [red]don't call you to trust this app[/], use it at your own risk \n"
              "but we recommend you more to install verified packages")
    return f"""{r['name']}{'✅' if r['verified'] else ''} by {r['authorName']}
{r['description']}
👍{r['likes']} | 👎{r['dislikes']}

{'''This package is not verified by the horsy team. This means that it
can be unstable or it can be malware. Most packages have unverified
state, but use it at your own risk.''' if not r['verified'] else
'''
This package is verified by the horsy team!
Keep in mind, developers can change the code after verification
We don't call you to trust this app, use it at your own risk
but we recommend you more to install verified packages
'''}
"""
