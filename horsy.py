import argparse
import os
import subprocess
import sys
from modules.core.request import request
import modules.cli.tui as tui
from modules.virustotal import add_to_cfg
from modules.core.exception import hook
import modules.core.vars as horsy_vars
import threading

sys.excepthook = hook
threading.excepthook = hook

# Getting the arguments
parser = argparse.ArgumentParser(description='horsy - the best package manager')
parser.add_argument('option', help='options for horsy (install/i | uninstall/un | updates/u | source/s | list/l | '
                                   'upload | search | info | like | dislike)',
                    choices=['install', 'i', 'uninstall', 'un', 'updates', 'u', 'source', 's', 'list', 'l', 'upload',
                             'search', 'info', 'like', 'dislike'],
                    nargs='?')
parser.add_argument('app', help='app to do function with', nargs='?')
parser.add_argument('--vt', help='your virustotal api key (account -> api key in VT)', dest='vt_key')

args = parser.parse_args()
option = args.option
app = args.app

# Window title
os.system('title horsy')

# Checking directories and files
if not os.path.exists(horsy_vars.horsypath + 'apps'):
    os.makedirs(horsy_vars.horsypath + 'apps')
if not os.path.isfile(horsy_vars.horsypath + 'config.cfg'):
    with open(horsy_vars.horsypath + 'config.cfg', 'w+') as f:
        f.write('{}')
if not os.path.isfile(horsy_vars.horsypath + 'apps/versions.json'):
    with open(horsy_vars.horsypath + 'apps/versions.json', 'w+') as f:
        f.write('{}')
if os.path.isfile(horsy_vars.horsypath + 'horsy.old'):
    os.remove(horsy_vars.horsypath + 'horsy.old')
    print('Removed old horsy')

# Checking version
try:
    with open(horsy_vars.horsypath + 'apps/version', 'r') as f:
        version = int(f.read())
except:
    print('Horsy may be not installed correctly. Please reinstall it or stop other horsy instances. '
          'If you installed it just now, please restart PC.')

if int(request.get('https://github.com/horsy-ml/horsy/raw/master/web_vars/version').text) > version:
    from ezzdl.download import dl
    import urllib.request
    print('New version available!')
    input('Press enter to update...')
    print('Updating...')
    print('Please wait...')
    os.rename(horsy_vars.horsypath + "horsy.exe", horsy_vars.horsypath + "horsy.old")
    print('Renamed horsy.exe to horsy.old')
    dl(['https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe',
        'https://github.com/horsy-ml/horsy/raw/master/bin/horsygui.exe']
       if os.path.isfile(horsy_vars.horsypath + 'horsygui.exe') else
       ['https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe'],
       horsy_vars.horsypath)
    urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                               horsy_vars.horsypath + '/apps/version')
    subprocess.Popen(str(horsy_vars.horsypath + 'horsy.exe'), shell=True, close_fds=True)
    sys.exit(0)


isNoArgs = False


# Function to display logo
def log_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    log_logo()
    option = ['install', 'uninstall', 'updates', 'source', 'list', 'upload', 'search', 'info'][
        tui.menu(['install app', 'uninstall app', 'see updates', 'get source',
                  'list of installed apps', 'upload your app', 'search for app',
                  'get information about app'])]
    isNoArgs = True

if not args.app and option not in ['list', 'l', 'upload', 'updates', 'u']:
    log_logo()
    print('\n')
    app = tui.get(f'Select app to {option}')

# Checking user option
match option:
    case 'upload':
        from modules.uploader import upload
        upload()
    case 'install' | 'i':
        from modules.cli.manager import install
        install(app)
    case 'uninstall' | 'un':
        from modules.cli.manager import uninstall
        uninstall(app)
    case 'updates' | 'u':
        from modules.updates import check
        update_list = check()
        if update_list:
            print('Use following commands to update apps: \n')
            for needs_update in update_list:
                print(f'horsy i {needs_update}')
        else:
            print('No updates available')
    case 'source' | 's':
        from modules.source import get_source
        get_source(app)
    case 'search':
        from modules.search import search
        search(app)
    case 'info':
        from modules.search import info
        info(app)
    case 'list' | 'l':
        from modules.cli.manager import apps_list
        apps_list()
    case 'like':
        from modules.liker import like
        like(app)
    case 'dislike':
        from modules.liker import dislike
        dislike(app)

if isNoArgs:
    input('[EXIT] Press enter to exit horsy...')
