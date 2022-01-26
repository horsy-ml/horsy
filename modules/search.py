import textwrap
from algoliasearch.search_client import SearchClient
import os
import requests
import modules.vars as horsy_vars
import json
from rich import print

client = SearchClient.create(
    requests.get('https://raw.githubusercontent.com/BarsTiger/horsy/master/web_vars/search_app').json()['APP_ID'],
    requests.get('https://raw.githubusercontent.com/BarsTiger/horsy/master/web_vars/search_app').json()['API_KEY'])
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
    r = requests.get(f"{horsy_vars.protocol}{horsy_vars.server_url}/packages/json/{package}").text
    if r == "":
        print(f"[red]Package {package} not found[/]")
        return
    try:
        r = json.loads(r)
    except:
        print("[red]Error with unsupported message[/]")
        return
    try:
        if r["message"] == "Internal server error":
            print("[red]Internal server error[/]")
            return
    except:
        pass

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
