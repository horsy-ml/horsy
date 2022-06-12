from ui.gui import Ui_MainWindow
from modules.core.qt_updater import call
from ezzthread import threaded
import modules.core.vars as horsy_vars
from ui.modules.setup_gui import fill_apps_list
import os


@threaded
def uninstall(package: str, ui: Ui_MainWindow) -> None:
    """
    Uninstall package
    :param package:
    :param ui:
    :return:
    """
    call(ui.installed_package_desc.clear)
    call(ui.installed_package_desc.setText, f'Uninstalling {package}...')
    if os.path.exists('{1}apps/{0}'.format(package, horsy_vars.horsypath)):
        os.system('rmdir /s /q "{1}apps/{0}"'.format(package, horsy_vars.horsypath))
        call(ui.installed_package_desc.append, "Files deleted")
    else:
        call(ui.installed_package_desc.append, f"App {package} is not installed or doesn't have files")
    if os.path.isfile('{1}apps/{0}.bat'.format(package, horsy_vars.horsypath)):
        os.remove("{1}apps/{0}.bat".format(package, horsy_vars.horsypath))
        call(ui.installed_package_desc.append, f"Launch script deleted")
    else:
        call(ui.installed_package_desc.append, f"App {package} is not installed or doesn't have launch script")
    fill_apps_list(ui)
    call(ui.installed_package_desc.append, f"Done!")
