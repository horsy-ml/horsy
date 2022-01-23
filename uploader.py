import json
import time
import requests
from rich import print
from auth import get_auth, del_auth
import re
import vars
import os


def matches(s):
    return re.match("^[a-z_-]*$", s) is not None


def urlmatch(s):
    return re.match("^https?://.*.(?:zip|exe)$", s) is not None


def upload():
    print('Welcome to the uploader')
    print('Before starting, please make sure you have done your project and [blink]uploaded[/] it to any hosting '
          'service or file sharing service')
    input('[OK] Press enter to continue...')
    auth = get_auth()
    print('Please enter the name of your project. It should contain only lowercase letters, '
          'underscores and dashes')
    project_name = None
    while project_name is None:
        project_name = input('> ')
        if not matches(project_name) or len(project_name) > 64 or len(project_name) < 3:
            print('[red]Invalid project name[/red]')
            project_name = None

    print('Please paste there project description. It should be a short text under 256 characters')
    description = None
    while description is None:
        description = input('> ')
        if len(description) > 256:
            print('[red]Description is too long[/red]')
            description = None

    print('Please paste there url of executable file. It should be a link to exe or zip file hosted somewhere. '
          'If app needs dependencies or specific launch options (python, node, etc), you can add them later')
    url = None
    while url is None:
        url = input('> ')
        if not urlmatch(url):
            print('[red]Invalid file url, also it should end on .exe or .zip[/red]')
            url = None

    print('Please paste there url of your project on GitHub or somewhere else. It should be a link to source code '
          'of your app. It can be archive, repository, site, whatever you want, optional but highly recommended.'
          'If you don\'t want to add it, just press Enter')
    source_url = input('> ')
    source_url = None if source_url == '' else source_url

    print('If your app needs any dependencies, please paste its link here. It can be exe of installer from official '
          'site. If you don\'t want to add it, just press Enter')
    download = None
    while download is None:
        download = input('> ')
        if download == '':
            download = None
            break
        if not urlmatch(download):
            print('[red]Invalid download url[/red]')
            download = None

    print('Please add which files should be run during installation. It should be an executable file name.'
          'If you don\'t want to add it, just press Enter')
    install = input('> ')
    install = None if install == '' else install

    print('Please specify main executable command. It can be executable file name (some-file.exe) or command, that '
          'launches your script (python some-file.py, etc)')
    run = None
    while run is None:
        run = input('> ')
        if run == '':
            print('[red]Please, specify runtime[/red]')
            run = None

    request = {
        'auth': auth,
        'name': project_name,
        'description': description,
        'url': url,
        'sourceUrl': source_url,
        'download': download,
        'install': install,
        'run': run
    }

    # request = {
    # "auth": {"email": "meshko_a@dlit.dp.ua", "password": "VeryGoodPassword"},
    # "name": "testapp",
    # "description": "Very good description",
    # # "url": "https://github.com/Cactus-0/cabanchik/raw/main/dist/cabanchik.exe",
    # "sourceUrl": "https://github.com/Cactus-0/cabanchik",
    # "download": "https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe",
    # "install": "python-3.10.2-amd64.exe",
    # "run": "cabanchik.exe"
    # }

    r = None
    while r is None:
        try:
            r = requests.post(vars.protocol + vars.server_url + '/packages/new', json=request).text
            r = json.loads(r)

            if r['message'] == 'Unauthorized':
                print('[red]Invalid credentials[/red]')
                print('Deleting auth from config')
                del_auth()
                request['auth'] = get_auth()
                print(r)
                r = None

            elif r['message'] == 'Internal server error':
                print('[red]Internal server error, request is broken[/red]')
                break

            elif r['message'] == 'Invalid body':
                print('[red]Invalid request body, try again[/red]')
                break

            elif r['message'] == 'Success':
                print('[green]Success, your project is created. You can install it by running[/] '
                      '[i]horsy install {0}[/]'.format(request['name']))
                break

            else:
                print('[red]Unknown error[/red]')
                print('Server response:')
                print(r)
                break
        except:
            with open(f'error_{time.time()}.txt', 'w') as f:
                f.write(str(r))
                print(f'[red]Something went wrong with unsupported error. You can check servers response in '
                      f'{os.getcwd()}/{f.name}[/red]')
            break
