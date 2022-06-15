# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 314)
        MainWindow.setMinimumSize(QtCore.QSize(488, 314))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/horsy_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical,\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(30, 30, 30);\n"
"    width: 10px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {    \n"
"    background-color: rgb(139, 139, 139);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:vertical:pressed,\n"
"QScrollBar::handle:horizontal:hover,\n"
"QScrollBar::handle:horizontal:pressed {    \n"
"    background-color: rgb(149, 149, 149);\n"
"}\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, \n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal,\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    background-color: #2c2d2e;\n"
"    min-height: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    border-width: 2px;\n"
"    background-color: #323232;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #262728;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #434343;\n"
"    border-color: #0000;\n"
"}\n"
"\n"
"\n"
"QLineEdit, QTextBrowser, QPlainTextEdit, QTextEdit {\n"
"    min-height: 30px;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    background-color: #242424;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"QListWidget {\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    padding: 10px;\n"
"    background-color: #242424;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QListWidget:item {\n"
"    background-color: #242424;\n"
"    selection-color: white;\n"
"}\n"
"QListWidget:item:hover {\n"
"    background-color: #323232;\n"
"}\n"
"QListWidget:item:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"    border-width: 1px;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    padding: 10px;\n"
"    background-color: #242424;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QTableWidget:item {\n"
"    background-color: #242424;\n"
"    selection-color: white;\n"
"}\n"
"QTableWidget:item:hover {\n"
"    background-color: #323232;\n"
"}\n"
"QTableWidget:item:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-style: solid;\n"
"    border-color: #303030;\n"
"    background-color: #2c2d2e;\n"
"    color: #ffffff;\n"
"}\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #434343;\n"
"    color: #656565;\n"
"    border-color: #434343;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    background-color: #323232;\n"
"}\n"
"QComboBox:on\n"
"{\n"
"    background-color: #434343;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #434343;\n"
"    color: #ffffff;\n"
"    selection-background-color: #777777;\n"
"    selection-color: white;\n"
"    outline: 0;\n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    border-radius: 6px; \n"
"}\n"
"\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background-color: #2c2d2e;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-color: #303030;\n"
"    padding: 5px;\n"
"}\n"
"QTabBar::tab:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"}\n"
"QTabWidget::pane \n"
"{\n"
"    background-color: #a0a0a0;\n"
"    color: #ffffff;\n"
"    border: 3px solid;\n"
"    border-radius: 15px;\n"
"    border-color: #1c1c1c;\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #262728;\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-color: #303030;\n"
"    padding: 5px;\n"
"}\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"}\n"
"QTabBar::tab:!selected \n"
"{\n"
"    background-color: #262626;\n"
"}\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"    background-color: #323232;\n"
"}\n"
"QTabBar::tab:top:!selected \n"
"{\n"
"    margin-top: 3px;\n"
"}\n"
"QTabBar::tab:bottom:!selected \n"
"{\n"
"    margin-bottom: 3px;\n"
"}\n"
"QTabBar::tab:top, QTabBar::tab:bottom \n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"QTabBar::tab:top:selected \n"
"{\n"
"    border-bottom-color: none;\n"
"}\n"
"QTabBar::tab:bottom:selected \n"
"{\n"
"    border-top-color: none;\n"
"}\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one \n"
"{\n"
"    margin-right: 0;\n"
"}\n"
"QTabBar::tab:left:!selected \n"
"{\n"
"    margin-right: 3px;\n"
"}\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 3px;\n"
"}\n"
"QTabBar::tab:left, QTabBar::tab:right \n"
"{\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"QTabBar::tab:left:selected \n"
"{\n"
"    border-left-color: none;\n"
"}\n"
"QTabBar::tab:right:selected \n"
"{\n"
"    border-right-color: none;\n"
"}\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one \n"
"{\n"
"    margin-bottom: 0;\n"
"}\n"
"\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #848484;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horsylogo_lay = QtWidgets.QWidget(self.centralwidget)
        self.horsylogo_lay.setObjectName("horsylogo_lay")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horsylogo_lay)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horsy_icon = QtWidgets.QLabel(self.horsylogo_lay)
        self.horsy_icon.setMinimumSize(QtCore.QSize(24, 24))
        self.horsy_icon.setMaximumSize(QtCore.QSize(24, 24))
        self.horsy_icon.setText("")
        self.horsy_icon.setPixmap(QtGui.QPixmap(":/img/horsy_white.png"))
        self.horsy_icon.setScaledContents(True)
        self.horsy_icon.setObjectName("horsy_icon")
        self.horizontalLayout_2.addWidget(self.horsy_icon)
        self.horsyname = QtWidgets.QLabel(self.horsylogo_lay)
        self.horsyname.setObjectName("horsyname")
        self.horizontalLayout_2.addWidget(self.horsyname)
        self.verticalLayout.addWidget(self.horsylogo_lay)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.path_box = QtWidgets.QLineEdit(self.widget)
        self.path_box.setObjectName("path_box")
        self.horizontalLayout_3.addWidget(self.path_box)
        self.choose_path_button = QtWidgets.QPushButton(self.widget)
        self.choose_path_button.setMinimumSize(QtCore.QSize(70, 32))
        self.choose_path_button.setObjectName("choose_path_button")
        self.horizontalLayout_3.addWidget(self.choose_path_button)
        self.verticalLayout.addWidget(self.widget)
        self.logsBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logsBrowser.setObjectName("logsBrowser")
        self.verticalLayout.addWidget(self.logsBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.buttons_widget = QtWidgets.QWidget(self.centralwidget)
        self.buttons_widget.setObjectName("buttons_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttons_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.install_horsy_button = QtWidgets.QPushButton(self.buttons_widget)
        self.install_horsy_button.setObjectName("install_horsy_button")
        self.horizontalLayout.addWidget(self.install_horsy_button)
        self.install_horsygui_button = QtWidgets.QPushButton(self.buttons_widget)
        self.install_horsygui_button.setEnabled(False)
        self.install_horsygui_button.setObjectName("install_horsygui_button")
        self.horizontalLayout.addWidget(self.install_horsygui_button)
        self.verticalLayout.addWidget(self.buttons_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "horsy installer"))
        self.horsyname.setText(_translate("MainWindow", "horsy installer"))
        self.path_box.setPlaceholderText(_translate("MainWindow", "Installation folder, apps will be stored here"))
        self.choose_path_button.setText(_translate("MainWindow", "Choose"))
        self.logsBrowser.setPlaceholderText(_translate("MainWindow", "Logs"))
        self.install_horsy_button.setText(_translate("MainWindow", "Install horsy"))
        self.install_horsygui_button.setText(_translate("MainWindow", "Install horsygui"))
import ui.img.images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
