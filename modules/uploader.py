import json
from modules.core.request import request
from rich import print
from modules.auth import get_auth, del_auth, get_auth_without_login
import re
import modules.core.vars as horsy_vars
from modules.core.http_status import handle
from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call


def matches(s):
    return re.match("^[a-z_-]*$", s) is not None


def urlmatch(s):
    return re.match("^https?://.*.(?:zip|exe|py|msi|js|bat|cmd|ps1)$", s) is not None


def fill_cli():
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
            print('[red]Invalid file url, also it should end on .exe, .zip, .py, .msi, .js, .bat, .cmd, .ps1[/red]')
            url = None

    print('Please paste there url of your project on GitHub or somewhere else. It should be a link to source code '
          'of your app. It can be archive, repository, site, whatever you want, optional but highly recommended.'
          'If you don\'t want to add it, just press Enter')
    source_url = (lambda x: None if x == '' else x)(input('> '))

    print('If your app needs any dependencies, please paste its link here. It can be exe of installer from official'
          ' site. If you don\'t want to add it, just press Enter')
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
    install = (lambda x: None if x == '' else x)(input('> '))

    print('Please specify main executable command. It can be executable file name ($appdir$\\some-file.exe) or '
          'command, that launches your script (python $appdir$\\some-file.py, cd $appdir$ & some-file.py etc). '
          '$appdir$ will be replaced with application directory. It is necessary to add!')
    run = None
    while run is None:
        run = input('> ')
        if run == '':
            print('[red]Please, specify runtime[/red]')
            run = None

    return {
            'auth': auth,
            'name': project_name,
            'description': description,
            'url': url,
            'sourceUrl': source_url,
            'download': download,
            'install': install,
            'run': run
        }


def fill_gui(ui: Ui_MainWindow):
    auth = get_auth_without_login()

    project_name = ui.new_package_name_box.text()
    if not matches(project_name) or len(project_name) > 64 or len(project_name) < 3:
        call(ui.upload_result_label.show)
        call(ui.upload_result_label.setText, 'Invalid project name')
        return

    description = ui.new_package_desc_box.toPlainText()
    if len(description) > 256:
        call(ui.upload_result_label.show)
        call(ui.upload_result_label.setText, 'Description is too long')
        return

    url = ui.new_package_exe_url_box.text()
    if not urlmatch(url):
        call(ui.upload_result_label.show)
        call(ui.upload_result_label.setText, 'Invalid file url')
        return

    download = ui.new_package_dep_url_box.text()
    if download == '':
        download = None
    elif not urlmatch(download):
        call(ui.upload_result_label.show)
        call(ui.upload_result_label.setText, 'Invalid download url')
        return

    run = ui.new_package_command_box.text()
    if run == '':
        call(ui.upload_result_label.show)
        call(ui.upload_result_label.setText, 'Please, specify runtime')
        return

    return dict({
            'auth': auth,
            'name': project_name,
            'description': description,
            'url': url,
            'sourceUrl': (lambda x: None if x == '' else x)(ui.new_package_source_box.text()),
            'download': download,
            'install': (lambda x: None if x == '' else x)(ui.new_package_dep_run_box.text()),
            'run': run
        })


def upload(ui: Ui_MainWindow = None):
    if not ui:
        request_body = fill_cli()
    else:
        request_body = fill_gui(ui)
        if request_body is None:
            return

    r = request.post(horsy_vars.url + '/packages/new', json=request_body)
    r_code = handle(r.status_code)
    r = r.text
    r = json.loads(r)

    if r_code[1] in [403, 401]:
        print('[red]Invalid credentials[/red]')
        print('Deleting auth from config')
        del_auth()
        request_body['auth'] = get_auth(ui)
        print(r)
        r = None
        if ui:
            return

    elif r_code[1] in [200, 201]:
        print('[green]Success, your project is created. You can install it by running[/] '
              '[i]horsy i {0}[/]'.format(request_body['name']))
        call(ui.upload_result_label.show)
        call(ui.upload_result_label.setText,
             'Success, your project is created. You can install it by running horsy i {0}'
             .format(request_body['name']))
        return

    call(ui.upload_result_label.show)
    call(ui.upload_result_label.setText, f'{r_code[0]}: {r.get("message")}')
