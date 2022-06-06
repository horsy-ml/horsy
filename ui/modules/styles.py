centralwidget_b = """
QWidget {
    background-color: rgba(30, 30, 30, 0.1);
    color: white;
    font: 10pt "Segoe UI";
}


QScrollBar:vertical,
QScrollBar:horizontal {
    border: none;
    background: rgba(30, 30, 30, 0);
    width: 10px;
    margin: 15px 0 15px 0;
    border-radius: 0px;
}

QScrollBar::handle:vertical,
QScrollBar::handle:horizontal {	
    background-color: rgba(139, 139, 139, 0);
    min-height: 30px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover,
QScrollBar::handle:vertical:pressed,
QScrollBar::handle:horizontal:hover,
QScrollBar::handle:horizontal:pressed {	
    background-color: rgba(149, 149, 149, 0);
}

QScrollBar::sub-line:vertical,
QScrollBar::add-line:vertical,
QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    height: 0px;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, 
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}


QPushButton {
    color: white;
    border-width: 1px;
    border-radius:6px;
    border-style: solid;
    border-color: rgba(48, 48, 48, 0.5);
    background-color: rgba(44, 45, 46, 0.3);
}
QPushButton:hover {
    border-width: 2px;
    background-color: rgba(50, 50, 50, 0.7);
}
QPushButton:pressed {
    background-color: rgba(38, 39, 40, 0.7);
}
QPushButton:disabled {
    background-color: rgba(67, 67, 67, 0.7);
    border-color: rgba(0, 0, 0, 0.7);
}


QLineEdit, QTextBrowser, QPlainTextEdit, QTextEdit {
    border-width: 1px;
    border-radius: 5px;
    border-style: solid;
    border-color: rgba(48, 48, 48);
    background-color: rgba(36, 36, 36, 0);
    font: 10pt "Segoe UI";
}


QListWidget {
    border-width: 1px;
    border-radius: 15px;
    border-style: solid;
    border-color: rgba(48, 48, 48);
    padding: 10px;
    background-color: rgba(100, 100, 100, 0);
    font: 10pt "Segoe UI";
}
QListWidget:item {
    background-color: rgba(36, 36, 36, 0);
    selection-color: white;
}
QListWidget:item:hover {
    background-color: rgba(50, 50, 50, 0);
}
QListWidget:item:selected {
    background-color: rgba(119, 119, 119, 1);
}


QComboBox
{
    border-width: 1px;
    border-radius:6px;
    border-style: solid;
    border-color: rgba(48, 48, 48);
    background-color: rgba(44, 45, 46, 0);
    color: white;
}

QComboBox::disabled
{
    background-color: rgba(67, 67, 67, 0);
    color: #656565;
    border-color: rgba(67, 67, 67);
}

QComboBox:hover
{
    background-color: rgba(50, 50, 50, 0);
}

QComboBox:on
{
    background-color: rgba(67, 67, 67, 0);
}

QComboBox QAbstractItemView
{
    background-color: rgba(67, 67, 67, 0);
    color: #ffffff;
    selection-background-color: rgba(119, 119, 119, 0);
    selection-color: white;
    outline: 0;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    border-radius: 6px; 
}


QTabBar::tab
{
    background-color: rgba(44, 45, 46, 0);
    color: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-color: rgba(48, 48, 48);
    padding: 5px;
}

QTabBar::tab:disabled
{
    background-color: rgba(101, 101, 101, 0);
    color: #656565;
}

QTabWidget::pane 
{
    background-color: rgba(160, 160, 160, 0);
    color: #ffffff;
    border: 3px solid;
    border-radius: 15px;
    border-color: rgba(28, 28, 28);
}

QTabBar::tab:selected
{
    background-color: rgba(38, 39, 40, 0);
    color: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-color: rgba(48, 48, 48);
    padding: 5px;
}

QTabBar::tab:selected:disabled
{
    background-color: rgba(64, 64, 64, 0);
    color: #656565;
}

QTabBar::tab:!selected 
{
    background-color: rgba(38, 38, 38, 0);
}

QTabBar::tab:!selected:hover 
{
    background-color: rgba(50, 50, 50, 0);
}

QTabBar::tab:top:!selected 
{
    margin-top: 3px;
}

QTabBar::tab:bottom:!selected 
{
    margin-bottom: 3px;
}

QTabBar::tab:top, QTabBar::tab:bottom 
{
    min-width: 8ex;
    margin-right: -1px;
    padding: 5px 10px 5px 10px;
}

QTabBar::tab:top:selected 
{
    border-bottom-color: none;
}

QTabBar::tab:bottom:selected 
{
    border-top-color: none;
}

QTabBar::tab:top:last, QTabBar::tab:bottom:last,
QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one 
{
    margin-right: 0;
}

QTabBar::tab:left:!selected 
{
    margin-right: 3px;
}

QTabBar::tab:right:!selected
{
    margin-left: 3px;
}

QTabBar::tab:left, QTabBar::tab:right 
{
    min-height: 8ex;
    margin-bottom: -1px;
    padding: 10px 5px 10px 5px;
}

QTabBar::tab:left:selected 
{
    border-left-color: none;
}

QTabBar::tab:right:selected 
{
    border-right-color: none;
}

QTabBar::tab:left:last, QTabBar::tab:right:last,
QTabBar::tab:left:only-one, QTabBar::tab:right:only-one 
{
    margin-bottom: 0;
}
"""

centralwidget_g = """
QWidget {
    background-color: rgb(30, 30, 30);
    color: rgb(255, 255, 255);
    font: 10pt "Segoe UI";
}
QScrollBar:vertical,
QScrollBar:horizontal {
    border: none;
    background: rgb(30, 30, 30);
    width: 10px;
    margin: 15px 0 15px 0;
    border-radius: 0px;
}
QScrollBar::handle:vertical,
QScrollBar::handle:horizontal {	
    background-color: rgb(139, 139, 139);
    min-height: 30px;
    border-radius: 5px;
}
QScrollBar::handle:vertical:hover,
QScrollBar::handle:vertical:pressed,
QScrollBar::handle:horizontal:hover,
QScrollBar::handle:horizontal:pressed {	
    background-color: rgb(149, 149, 149);
}
QScrollBar::sub-line:vertical,
QScrollBar::add-line:vertical,
QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    height: 0px;
}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, 
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
QPushButton {
    color: white;
    border-width: 1px;
    border-radius:6px;
    border-style: solid;
    border-color: #303030;
    background-color: #2c2d2e;
}
QPushButton:hover {
    border-width: 2px;
    background-color: #323232;
}
QPushButton:pressed {
    background-color: #262728;
}
QPushButton:disabled {
    background-color: #434343;
    border-color: #0000;
}
QLineEdit, QTextBrowser, QPlainTextEdit, QTextEdit {
    border-width: 1px;
    border-radius: 5px;
    border-style: solid;
    border-color: #303030;
    background-color: #242424;
    font: 10pt "Segoe UI";
}
QListWidget {
    border-width: 1px;
    border-radius: 15px;
    border-style: solid;
    border-color: #303030;
    padding: 10px;
    background-color: #242424;
    font: 10pt "Segoe UI";
}
QListWidget:item {
    background-color: #242424;
    selection-color: white;
}
QListWidget:item:hover {
    background-color: #323232;
}
QListWidget:item:selected {
    background-color: #777777;
}
QComboBox
{
    border-width: 1px;
    border-radius:6px;
    border-style: solid;
    border-color: #303030;
    background-color: #2c2d2e;
    color: #ffffff;
}
QComboBox::disabled
{
    background-color: #434343;
    color: #656565;
    border-color: #434343;
}
QComboBox:hover
{
    background-color: #323232;
}
QComboBox:on
{
    background-color: #434343;
}
QComboBox QAbstractItemView
{
    background-color: #434343;
    color: #ffffff;
    selection-background-color: #777777;
    selection-color: white;
    outline: 0;
}
QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    border-radius: 6px; 
}
QTabBar::tab
{
    background-color: #2c2d2e;
    color: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-color: #303030;
    padding: 5px;
}
QTabBar::tab:disabled
{
    background-color: #656565;
    color: #656565;
}
QTabWidget::pane 
{
    background-color: #a0a0a0;
    color: #ffffff;
    border: 3px solid;
    border-radius: 15px;
    border-color: #1c1c1c;
}
QTabBar::tab:selected
{
    background-color: #262728;
    color: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-color: #303030;
    padding: 5px;
}
QTabBar::tab:selected:disabled
{
    background-color: #404040;
    color: #656565;
}
QTabBar::tab:!selected 
{
    background-color: #262626;
}
QTabBar::tab:!selected:hover 
{
    background-color: #323232;
}
QTabBar::tab:top:!selected 
{
    margin-top: 3px;
}
QTabBar::tab:bottom:!selected 
{
    margin-bottom: 3px;
}
QTabBar::tab:top, QTabBar::tab:bottom 
{
    min-width: 8ex;
    margin-right: -1px;
    padding: 5px 10px 5px 10px;
}
QTabBar::tab:top:selected 
{
    border-bottom-color: none;
}
QTabBar::tab:bottom:selected 
{
    border-top-color: none;
}
QTabBar::tab:top:last, QTabBar::tab:bottom:last,
QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one 
{
    margin-right: 0;
}
QTabBar::tab:left:!selected 
{
    margin-right: 3px;
}
QTabBar::tab:right:!selected
{
    margin-left: 3px;
}
QTabBar::tab:left, QTabBar::tab:right 
{
    min-height: 8ex;
    margin-bottom: -1px;
    padding: 10px 5px 10px 5px;
}
QTabBar::tab:left:selected 
{
    border-left-color: none;
}
QTabBar::tab:right:selected 
{
    border-right-color: none;
}
QTabBar::tab:left:last, QTabBar::tab:right:last,
QTabBar::tab:left:only-one, QTabBar::tab:right:only-one 
{
    margin-bottom: 0;
}
"""
