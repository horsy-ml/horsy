from modules.core.qt_updater import call
from ui.gui import Ui_MainWindow
from modules.virustotal import get_report, scan_file, get_key


def scan_to_gui(ui: Ui_MainWindow, filename: str) -> dict[str, dict[str, int], dict[str, str]]:
    if not get_key():
        call(ui.search_package_desc.append, "")
        call(ui.search_package_desc.append, f"Virustotal api key not found")
        call(ui.search_package_desc.append, f"You can add it by entering horsy --vt [your key] in terminal "
                                            f"or on settings tab")
        call(ui.search_package_desc.append, "")

    else:
        call(ui.search_package_desc.append, "")
        call(ui.search_package_desc.append, f"Virustotal api key found")
        call(ui.search_package_desc.append, f"Starting virustotal scan, it may take a while")
        call(ui.search_package_desc.append, f"If you want to disable scan, type horsy --vt disable in terminal "
                                            f"or remove key on settings tab")

        scan_file(filename)
        call(ui.search_package_desc.append, f"Virustotal scan finished")

        analysis = get_report(filename)
        call(ui.search_package_desc.append, f"You can see report by opening: {analysis['link']}")
        call(ui.search_package_desc.append,
             f"{analysis['detect']['malicious']} antivirus flagged this file as malicious")
        call(ui.search_package_desc.append, "")

        return analysis
