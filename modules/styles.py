centralwidget = """
QWidget {
    background-color: rgb(30, 30, 30);
}

QScrollBar:vertical {
    border: none;
    background: rgb(30, 30, 30);
    width: 10px;
    margin: 15px 0 15px 0;
    border-radius: 0px;
}

QScrollBar::handle:vertical {	
    background-color: rgb(139, 139, 139);
    min-height: 30px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover,
QScrollBar::handle:vertical:pressed {	
    background-color: rgb(149, 149, 149);
}

QScrollBar::sub-line:vertical,
QScrollBar::add-line:vertical,
QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    height: 0px;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{
    background: none;
}
"""

tabwidget = """
QTabBar::tab {
    background: rgb(22, 22, 22);
    color: white;  
    font: 12pt \"MS Shell Dlg 2\";
    width: 150px;
    height: 21px;
    padding: 13px;
}
QTabBar::tab:selected {
    color: rgb(166, 184, 200);
    background: rgb(45, 45, 45);
}
QTabBar::tab:hover {
    color: rgb(166, 184, 200);
    background: rgb(29, 29, 29);
}
QTabBar {
    margin-top: 5px;
}
"""

button = """
QPushButton {
    color: rgb(204, 204, 204);
    border-width: 1px;
    border-radius:6px;
    border-style: solid;
    background-color: rgb(28, 30, 33);
    border-color: rgb(66, 143, 225);
}
QPushButton:hover {
    border-width: 2px;
}
QPushButton:pressed {
    background-color: rgb(50, 60, 63);
}
QPushButton:disabled {
    border-width: 0px;
    background-color: rgb(92, 99, 109);
}
"""
