import argparse
import tui as tui
from console import cls
from manager import *
from virustotal import add_to_cfg
from uploader import upload

# Getting the arguments
parser = argparse.ArgumentParser(description='horsy - the best package manager')
parser.add_argument('option', help='options for horsy (install/i | uninstall/un | source/s | update/u | list/l | '
                                   'upload)',
                    choices=['install', 'i', 'uninstall', 'un', 'source', 's', 'update', 'u', 'list', 'l', 'upload',
                             'search'],
                    nargs='?')
parser.add_argument('app', help='app to install/uninstall/download source', nargs='?')
parser.add_argument('--vt', help='your virustotal api key (account -> api key in VT)', dest='vt_key')

args = parser.parse_args()
option = args.option
app = args.app

# Checking if the user has a new VT key
if args.vt_key:
    if args.vt_key != 'disable':
        add_to_cfg(args.vt_key)
    else:
        add_to_cfg(None)

# Checking directories and files
if not os.path.exists('apps'):
    os.makedirs('apps')
if not os.path.exists('sources'):
    os.makedirs('sources')
if not os.path.isfile('config.cfg'):
    with open('config.cfg', 'w') as f:
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

# Checking if arguments are empty to use in-app CLI
if not args.option:
    option = ['install', 'uninstall', 'source', 'update', 'list', 'upload', 'search'][
        tui.menu(['install app', 'uninstall app', 'get source', 'update app', 'list of installed apps',
                  'upload your app', 'search for app'])]
    isNoArgs = True

if not args.app:
    if option not in ['list', 'upload']:
        print('\n')
        app = tui.get(f'Select app to {option}')

if option in 'upload':
    upload()

if option in ['install', 'i']:
    install(app)

if option in ['uninstall', 'un']:
    uninstall(app)

if isNoArgs:
    input('[EXIT] Press enter to exit horsy...')
