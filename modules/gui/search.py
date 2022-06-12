from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
from ezzthread import threaded
from modules.search import info
from modules.search import search


@threaded
def search_for_package(ui: Ui_MainWindow) -> None:
    """
    Search for package
    :param ui:
    :return:
    """
    package = ui.search_box.text()
    call(ui.search_packages_list.clear)
    call(ui.search_packages_list.addItems, search(package, True))


@threaded
def display_info(ui: Ui_MainWindow) -> None:
    """
    Display info
    :param ui:
    :return:
    """
    ui.search_packages_from_list_lay.show()
    call(ui.search_package_desc.setText, 'Loading...')
    call(ui.search_package_desc.setText, info(ui.search_packages_list.currentItem().text()))
