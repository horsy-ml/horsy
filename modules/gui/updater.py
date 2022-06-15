import modules.core.vars as horsy_vars
from ui.updater import Ui_MainWindow
from modules.core.request import request
from ezzthread import threaded
import threading
import sys
import os


def needs_update() -> bool:
    with open(horsy_vars.horsypath + 'apps/version', 'r') as f:
        return int(request.get('https://github.com/horsy-ml/horsy/raw/master/web_vars/version').text) > int(f.read())


@threaded
def update(ui: Ui_MainWindow):
    from modules.gui.downloader import download_url
    import urllib.request

    threads = [
        threading.Thread(target=download_url,
                         args=(ui.progressBar_cli, None,
                               'https://github.com/horsy-ml/horsy/raw/master/bin/horsy.exe',
                               horsy_vars.horsypath + 'horsy.new')
                         ),
        threading.Thread(target=download_url,
                         args=(ui.progressBar_gui, None,
                               'https://github.com/horsy-ml/horsy/raw/master/bin/horsygui.exe',
                               horsy_vars.horsypath + 'horsygui.new')
                         )
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    urllib.request.urlretrieve("https://github.com/horsy-ml/horsy/raw/master/web_vars/version",
                               horsy_vars.horsypath + '/apps/version')

    os.rename(horsy_vars.horsypath + "horsygui.exe", horsy_vars.horsypath + "horsygui.old")
    os.rename(horsy_vars.horsypath + "horsy.exe", horsy_vars.horsypath + "horsy.old")
    os.remove(horsy_vars.horsypath + "horsy.old")
    os.rename(horsy_vars.horsypath + "horsygui.new", horsy_vars.horsypath + "horsygui.exe")
    os.rename(horsy_vars.horsypath + "horsy.new", horsy_vars.horsypath + "horsy.exe")

    ui.launch_button.setEnabled(True)


def launch_new_horsy():
    import subprocess
    subprocess.Popen(horsy_vars.horsypath + "horsygui.exe", shell=True, close_fds=True)
    sys.exit(0)
