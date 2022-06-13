from ezzthread import threaded
from ui.gui import Ui_MainWindow
from modules.search import info
from modules.core.qt_updater import call


@threaded
def on_installed_click(ui: Ui_MainWindow) -> None:
    ui.installed_packages_from_list_lay.show()
    call(ui.installed_package_desc.setText, 'Loading...')
    call(ui.installed_package_desc.setText, info(ui.installed_packages_list.currentItem().text().replace('!', '')))
