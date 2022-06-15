from ezzthread import threaded
from ui.gui import Ui_MainWindow
from modules.data.settings import Settings
from modules.virustotal import add_to_cfg, get_key


@threaded
def save_settings(ui: Ui_MainWindow):
    Settings.update("animation", ui.choose_animation_box.currentText())
    Settings.update("theme", ui.choose_theme_box.currentText())
    add_to_cfg(ui.add_vt_key_box.text().strip() if ui.add_vt_key_box.text().strip() != '' else None)


@threaded
def fill_settings(ui: Ui_MainWindow):
    settings = Settings.get_settings()
    ui.choose_animation_box.setCurrentText(settings.get("animation"))
    ui.choose_theme_box.setCurrentText(settings.get("theme"))
    ui.add_vt_key_box.setText(get_key())
