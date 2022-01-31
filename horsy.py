import argparse
import os
import sys
import requests
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

# Checking directories and files
if not os.path.exists(horsy_vars.horsypath + 'apps'):
    os.makedirs(horsy_vars.horsypath + 'apps')
if not os.path.isfile(horsy_vars.horsypath + 'config.cfg'):
    with open(horsy_vars.horsypath + 'config.cfg', 'w') as f:
        f.write('{}')

# Checking version
try:
    with open(horsy_vars.horsypath + 'apps/version', 'r') as f:
        version = int(f.read())
        if int(requests.get('https://github.com/BarsTiger/horsy/raw/master/web_vars/version').text) > version:
            print('New version available!')
            input('Press enter to update...')
            with open(os.path.join(horsy_vars.horsypath) + '/horsy_updater.exe', 'wb') as f:
                f.write(requests.get('https://github.com/BarsTiger/horsy/raw/master/bin/horsy_updater.exe').content)
            os.system('horsy_updater.exe horsy')
            sys.exit(0)
except:
    print('Horsy may be not installed correctly. Please reinstall it.')


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

if option in ['like']:
    from modules.liker import like
    like(app)

if option in ['dislike']:
    from modules.liker import dislike
    dislike(app)

if isNoArgs:
    input('[EXIT] Press enter to exit horsy...')
