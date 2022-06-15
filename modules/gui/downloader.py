import os.path
from functools import partial
from urllib.request import urlopen
from urllib.parse import unquote
from PyQt5.QtWidgets import QProgressBar
from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
import threading


def download_url(bar: QProgressBar, ui: Ui_MainWindow, url: str, path: str) -> None:
    call(ui.search_package_desc.append, f"Requesting {url}")
    response = urlopen(url)
    call(bar.setMaximum, 100)
    call(bar.setValue, 0)
    size = int(response.info()["Content-length"])
    downloaded = 0
    with open(path, "wb") as dest_file:
        for data in iter(partial(response.read, 4096), b""):
            downloaded += len(data)
            dest_file.write(data)
            call(bar.setValue, int(downloaded / size * 100))
    call(ui.search_package_desc.append, f"Downloaded {os.path.abspath(path)}")


def dl(ui: Ui_MainWindow, url: str, dest_dir: str, dep_url: str = None) -> None:
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    threads = list()
    threads.append(
        threading.Thread(target=download_url,
                         args=(ui.downloading_main_file_progress, ui, url, os.path.join(dest_dir,
                                                                                        unquote(url.split('/')[-1]))))
    )
    call(ui.downloading_main_file_progress.show)
    if dep_url:
        threads.append(
            threading.Thread(target=download_url, args=(ui.downloading_dependency_progress, ui, dep_url,
                                                        dest_dir + "/" + unquote(dep_url.split("/")[-1]))
                             )
        )
        call(ui.downloading_dependency_progress.show)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
