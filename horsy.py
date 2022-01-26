import argparse
import os
import sys

import modules.tui as tui
from modules.console import cls
from modules.virustotal import add_to_cfg
import modules.vars as horsy_vars

# Getting the arguments
parser = argparse.ArgumentParser(description='horsy - the best package manager')
parser.add_argument('option', help='options for horsy (install/i | uninstall/un | source/s | update/u | list/l | '
                                   'upload | search | info | like | dislike)',
                    choices=['install', 'i', 'uninstall', 'un', 'source', 's', 'update', 'u', 'list', 'l', 'upload',
                             'search', 'info', 'like', 'dislike'],
                    nargs='?')
parser.add_argument('app', help='app to do function with', nargs='?')
parser.add_argument('--vt', help='your virustotal api key (account -> api key in VT)', dest='vt_key')

args = parser.parse_args()
option = args.option
app = args.app

# Checking directories and files
if not os.path.exists(horsy_vars.horsypath + 'apps'):
    os.makedirs(horsy_vars.horsypath + 'apps')
if not os.path.isfile(horsy_vars.horsypath + 'config.cfg'):
    with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
        f.write('{}')

# Displaying the logo
os.system('title horsy')
cls()
print('''
 __   __  _______  ______    _______  __   __ 
|  | |  ||       ||    _ |  |       ||  | |  |
|  |_|  ||   _   ||   | ||  |  _____||  |_|  |
|       ||  | |  ||   |_||_ | |_____ |       |
|       ||  |_|  ||    __  ||_____  ||_     _|
|   _   ||       ||   |  | | _____| |  |   |  
|__| |__||_______||___|  |_||_______|  |___|  
        Search powered by Algolia
''')
isNoArgs = False

# Checking if the user has a new VT key
if args.vt_key:
    if args.vt_key != 'disable':
        add_to_cfg(args.vt_key)
        print('VT key updated')
    else:
        print('VT disabled')
        add_to_cfg(None)
    sys.exit()

# Checking if arguments are empty to use in-app CLI
if not args.option:
    option = ['install', 'uninstall', 'source', 'update', 'list', 'upload', 'search', 'info'][
        tui.menu(['install app', 'uninstall app', 'get source', 'update app', 'list of installed apps',
                  'upload your app', 'search for app', 'get information about app'])]
    isNoArgs = True

if not args.app:
    if option not in ['list', 'upload', 'update']:
        print('\n')
        app = tui.get(f'Select app to {option}')

# Checking user option (Yanderedev method)
if option in 'upload':
    from modules.uploader import upload
    upload()

if option in ['install', 'i']:
    from modules.manager import install
    install(app)

if option in ['uninstall', 'un']:
    from modules.manager import uninstall
    uninstall(app)

if option in ['source', 's']:
    from modules.source import get_source
    get_source(app)

if option in ['search']:
    from modules.search import search
    search(app)

if option in ['info']:
    from modules.search import info
    info(app)

if option in ['list', 'l']:
    from modules.manager import apps_list
    apps_list()

if isNoArgs:
    input('[EXIT] Press enter to exit horsy...')
