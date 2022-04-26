from PyQt5 import QtCore, QtGui, QtWidgets
import modules.images  # import images from binaries
import ctypes


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 700)
        MainWindow.setMinimumSize(QtCore.QSize(899, 700))
        MainWindow.setMaximumSize(QtCore.QSize(899, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/horsy_white32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.99)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("""QWidget{\n"
    background-color: rgb(30, 30, 30);
}
QScrollBar:horizontal {
    border: none;
    background: rgb(52, 59, 72);
    height: 8px;
    margin: 0px 21px 0 21px;
    border-radius: 0px;
}
QScrollBar::handle:horizontal {
    background: rgb(47, 48, 50);
    min-width: 25px;
    border-radius: 4px
}
QScrollBar::add-line:horizontal {
    border: none;
    background: rgb(55, 63, 77);
    width: 20px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
    border: none;
    background: rgb(55, 63, 77);
    width: 20px;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
     background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
     background: none;
}
QScrollBar:vertical {
    border: none;
    background: rgb(52, 59, 72);
    width: 8px;
    margin: 21px 0 21px 0;
    border-radius: 0px;
}
 QScrollBar::handle:vertical {	
    background: rgb(47, 48, 50);
    min-height: 25px;
    border-radius: 4px
 }
 QScrollBar::add-line:vertical {
    border: none;
    background: transparent;
    height: 10px;
    border-radius: 4px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
 }
 QScrollBar::sub-line:vertical {
    border: none;
    background: transparent;
    height: 10px;
    border-radius: 4px;
    subcontrol-position: top;
    subcontrol-origin: margin;
 }
 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
     background: none;
 }

 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none;
 }

""")
        self.centralwidget.setObjectName("centralwidget")
        self.horsy_logo_lefttop = QtWidgets.QLabel(self.centralwidget)
        self.horsy_logo_lefttop.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.horsy_logo_lefttop.setStyleSheet("background: none;")
        self.horsy_logo_lefttop.setText("")
        self.horsy_logo_lefttop.setPixmap(QtGui.QPixmap(":/images/horsy_white32x32.png"))
        self.horsy_logo_lefttop.setObjectName("horsy_logo_lefttop")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 4, 881, 691))
        self.tabWidget.setToolTip("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab\n"
                                     "{\n"
                                     "    background: rgb(22, 22, 22);\n"
                                     "    color: white;  \n"
                                     "    font: 12pt \"MS Shell Dlg 2\";\n"
                                     "    width: 150px;\n"
                                     "    height: 21px;\n"
                                     "    padding: 13px;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected\n"
                                     "{\n"
                                     "    color: rgb(166, 184, 200);\n"
                                     "    background: rgb(45, 45, 45);\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:hover \n"
                                     "{\n"
                                     "    color: rgb(166, 184, 200);\n"
                                     "    background: rgb(29, 29, 29);\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar\n"
                                     "{\n"
                                     "margin-top: 5px;\n"
                                     "}\n"
                                     "")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.account_tab = QtWidgets.QWidget()
        self.account_tab.setObjectName("account_tab")
        self.loginlogout_button = QtWidgets.QPushButton(self.account_tab)
        self.loginlogout_button.setEnabled(True)
        self.loginlogout_button.setGeometry(QtCore.QRect(720, 10, 151, 50))
        self.loginlogout_button.setMinimumSize(QtCore.QSize(0, 50))
        self.loginlogout_button.setStyleSheet("QPushButton {\n"
                                              "    color: rgb(204, 204, 204);\n"
                                              "    border-width: 1px;\n"
                                              "    border-radius:6px;\n"
                                              "    border-style: solid;\n"
                                              "    background-color: rgb(28, 30, 33);\n"
                                              "    border-color: rgb(66, 143, 225);\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "    border-width: 2px;\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(50, 60, 63);\n"
                                              "}\n"
                                              "QPushButton:disabled{\n"
                                              "    border-width: 0px;\n"
                                              "    background-color: rgb(92, 99, 109);\n"
                                              "}")
        self.loginlogout_button.setObjectName("loginlogout_button")
        self.username_box = QtWidgets.QLineEdit(self.account_tab)
        self.username_box.setGeometry(QtCore.QRect(720, 70, 151, 31))
        self.username_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                        "border-radius: 5px;    \n"
                                        "color: rgb(242, 242, 242);\n"
                                        "padding: 0px 5px 0px 5px;\n")
        self.username_box.setText("Log in first")
        self.username_box.setReadOnly(True)
        self.username_box.setObjectName("username_box")
        self.regmessage_box = QtWidgets.QLineEdit(self.account_tab)
        self.regmessage_box.setGeometry(QtCore.QRect(720, 110, 151, 31))
        self.regmessage_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                          "border-radius: 5px;    \n"
                                          "color: rgb(27, 166, 221);")
        self.regmessage_box.setText(" Still not registered? Click here")
        self.regmessage_box.setReadOnly(True)
        self.regmessage_box.setObjectName("regmessage_box")
        self.regmessage_button = QtWidgets.QPushButton(self.account_tab)
        self.regmessage_button.setGeometry(QtCore.QRect(720, 110, 151, 31))
        self.regmessage_button.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
                                             "border-color: rgb(0, 0, 0, 0);\n"
                                             "color: rgb(0, 0, 0, 0);")
        self.regmessage_button.setText("")
        self.regmessage_button.setObjectName("regmessage_button")
        self.requestupdate_button = QtWidgets.QPushButton(self.account_tab)
        self.requestupdate_button.setGeometry(QtCore.QRect(225, 590, 200, 40))
        self.requestupdate_button.setStyleSheet("QPushButton {\n"
                                                "    color: rgb(204, 204, 204);\n"
                                                "    border-width: 1px;\n"
                                                "    border-radius:6px;\n"
                                                "    border-style: solid;\n"
                                                "    background-color: rgb(28, 30, 33);\n"
                                                "    border-color: rgb(66, 143, 225);\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    border-width: 2px;\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "    background-color: rgb(50, 60, 63);\n"
                                                "}\n"
                                                "QPushButton:disabled{\n"
                                                "    border-width: 0px;\n"
                                                "    background-color: rgb(92, 99, 109);\n"
                                                "}")
        self.requestupdate_button.setText("Request selected package \nupdate on user side (dev)")
        self.requestupdate_button.setObjectName("requestupdate_button")
        self.editowned_button = QtWidgets.QPushButton(self.account_tab)
        self.editowned_button.setGeometry(QtCore.QRect(445, 590, 200, 40))
        self.editowned_button.setStyleSheet("QPushButton {\n"
                                            "    color: rgb(204, 204, 204);\n"
                                            "    border-width: 1px;\n"
                                            "    border-radius:6px;\n"
                                            "    border-style: solid;\n"
                                            "    background-color: rgb(28, 30, 33);\n"
                                            "    border-color: rgb(66, 143, 225);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    border-width: 2px;\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color: rgb(50, 60, 63);\n"
                                            "}\n"
                                            "QPushButton:disabled{\n"
                                            "    border-width: 0px;\n"
                                            "    background-color: rgb(92, 99, 109);\n"
                                            "}")
        self.editowned_button.setText("Edit selected package")
        self.editowned_button.setObjectName("requestupdate_button")
        self.changeemail_button = QtWidgets.QPushButton(self.account_tab)
        self.changeemail_button.setEnabled(True)
        self.changeemail_button.setGeometry(QtCore.QRect(360, 20, 151, 50))
        self.changeemail_button.setMinimumSize(QtCore.QSize(0, 50))
        self.changeemail_button.setStyleSheet("QPushButton {\n"
                                              "    color: rgb(204, 204, 204);\n"
                                              "    border-width: 1px;\n"
                                              "    border-radius:6px;\n"
                                              "    border-style: solid;\n"
                                              "    background-color: rgb(28, 30, 33);\n"
                                              "    border-color: rgb(66, 143, 225);\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "    border-width: 2px;\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(50, 60, 63);\n"
                                              "}\n"
                                              "QPushButton:disabled{\n"
                                              "    border-width: 0px;\n"
                                              "    background-color: rgb(92, 99, 109);\n"
                                              "}")
        self.changeemail_button.setObjectName("changeemail_button")
        self.email_box = QtWidgets.QTextEdit(self.account_tab)
        self.email_box.setEnabled(True)
        self.email_box.setGeometry(QtCore.QRect(10, 20, 341, 51))
        self.email_box.setStyleSheet("QTextEdit {\n"
                                     "    background-color: rgb(74, 76, 83);\n"
                                     "    border-radius: 5px;    \n"
                                     "    color: rgb(242, 242, 242);\n"
                                     "    padding: 15px, 15px;\n"
                                     "    border: 15px white;\n"
                                     "}")
        self.email_box.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.email_box.setAcceptRichText(False)
        self.email_box.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.email_box.setObjectName("email_box")
        self.oldpass_box = QtWidgets.QTextEdit(self.account_tab)
        self.oldpass_box.setEnabled(True)
        self.oldpass_box.setGeometry(QtCore.QRect(10, 80, 341, 51))
        self.oldpass_box.setStyleSheet("QTextEdit {\n"
                                       "    background-color: rgb(74, 76, 83);\n"
                                       "    border-radius: 5px;    \n"
                                       "    color: rgb(242, 242, 242);\n"
                                       "    padding: 15px, 15px;\n"
                                       "    border: 15px white;\n"
                                       "}")
        self.oldpass_box.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.oldpass_box.setAcceptRichText(False)
        self.oldpass_box.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.oldpass_box.setObjectName("oldpass_box")
        self.newpass_box = QtWidgets.QTextEdit(self.account_tab)
        self.newpass_box.setEnabled(True)
        self.newpass_box.setGeometry(QtCore.QRect(10, 140, 341, 51))
        self.newpass_box.setStyleSheet("QTextEdit {\n"
                                       "    background-color: rgb(74, 76, 83);\n"
                                       "    border-radius: 5px;    \n"
                                       "    color: rgb(242, 242, 242);\n"
                                       "    padding: 15px, 15px;\n"
                                       "    border: 15px white;\n"
                                       "}")
        self.newpass_box.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.newpass_box.setAcceptRichText(False)
        self.newpass_box.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.newpass_box.setObjectName("newpass_box")
        self.changepass_button = QtWidgets.QPushButton(self.account_tab)
        self.changepass_button.setEnabled(True)
        self.changepass_button.setGeometry(QtCore.QRect(360, 140, 151, 50))
        self.changepass_button.setMinimumSize(QtCore.QSize(0, 50))
        self.changepass_button.setStyleSheet("QPushButton {\n"
                                             "    color: rgb(204, 204, 204);\n"
                                             "    border-width: 1px;\n"
                                             "    border-radius:6px;\n"
                                             "    border-style: solid;\n"
                                             "    background-color: rgb(28, 30, 33);\n"
                                             "    border-color: rgb(66, 143, 225);\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    border-width: 2px;\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    background-color: rgb(50, 60, 63);\n"
                                             "}\n"
                                             "QPushButton:disabled{\n"
                                             "    border-width: 0px;\n"
                                             "    background-color: rgb(92, 99, 109);\n"
                                             "}")
        self.changepass_button.setObjectName("changepass_button")
        self.manage_packages_table = QtWidgets.QTableWidget(self.account_tab)
        self.manage_packages_table.setGeometry(QtCore.QRect(10, 240, 871, 351))
        self.manage_packages_table.setStyleSheet("QTableWidget\n"
                                                 "{\n"
                                                 "color: white;\n"
                                                 "font: 15pt \"MS Shell Dlg 2\";\n"
                                                 "margin: 20px;\n"
                                                 "border-radius: 45px;\n"
                                                 "}\n"
                                                 "")
        self.manage_packages_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.manage_packages_table.setAutoScroll(False)
        self.manage_packages_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.manage_packages_table.setTabKeyNavigation(False)
        self.manage_packages_table.setProperty("showDropIndicator", False)
        self.manage_packages_table.setDragDropOverwriteMode(False)
        self.manage_packages_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.manage_packages_table.setShowGrid(False)
        self.manage_packages_table.setObjectName("installed_table")
        self.manage_packages_table.horizontalHeader().setVisible(False)
        self.manage_packages_table.horizontalHeader().setDefaultSectionSize(203)
        self.manage_packages_table.horizontalHeader().setHighlightSections(False)
        self.manage_packages_table.horizontalHeader().setMinimumSectionSize(150)
        self.manage_packages_table.verticalHeader().setVisible(False)
        self.manage_packages_table.verticalHeader().setDefaultSectionSize(120)
        self.manage_packages_table.verticalHeader().setHighlightSections(False)
        self.manage_packages_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.manage_packages_table.setColumnCount(0)
        self.manage_packages_table.setRowCount(0)
        self.manage_packages_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.manage_packages_message = QtWidgets.QTextBrowser(self.account_tab)
        self.manage_packages_message.setGeometry(QtCore.QRect(380, 230, 121, 21))
        self.manage_packages_message.setStyleSheet("color: white;\n"
                                                   "border: none;")
        self.manage_packages_message.setAcceptRichText(False)
        self.manage_packages_message.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.manage_packages_message.setObjectName("manage_packages_message")
        self.tabWidget.addTab(self.account_tab, "")
        self.upload_tab = QtWidgets.QWidget()
        self.upload_tab.setObjectName("upload_tab")
        self.packagename_box = QtWidgets.QLineEdit(self.upload_tab)
        self.packagename_box.setGeometry(QtCore.QRect(10, 55, 101, 31))
        self.packagename_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                           "border-radius: 5px;    \n"
                                           "color: rgb(242, 242, 242);")
        self.packagename_box.setObjectName("packagename_box")
        self.before_uploading_message = QtWidgets.QTextBrowser(self.upload_tab)
        self.before_uploading_message.setGeometry(QtCore.QRect(10, 10, 321, 41))
        self.before_uploading_message.setStyleSheet("color: white;\n"
                                                    "border: none;")
        self.before_uploading_message.setAcceptRichText(False)
        self.before_uploading_message.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.before_uploading_message.setObjectName("before_uploading_message")
        self.packagename_message = QtWidgets.QTextBrowser(self.upload_tab)
        self.packagename_message.setGeometry(QtCore.QRect(120, 60, 321, 21))
        self.packagename_message.setStyleSheet("color: white;\n"
                                               "border: none;")
        self.packagename_message.setAcceptRichText(False)
        self.packagename_message.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.packagename_message.setObjectName("packagename_message")
        self.package_desc_box = QtWidgets.QTextBrowser(self.upload_tab)
        self.package_desc_box.setGeometry(QtCore.QRect(10, 90, 256, 101))
        self.package_desc_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                            "border-radius: 5px;    \n"
                                            "color: rgb(242, 242, 242);")
        self.package_desc_box.setAcceptRichText(False)
        self.package_desc_box.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction
            | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse)
        self.package_desc_box.setObjectName("package_desc_box")
        self.url_of_exe_box = QtWidgets.QLineEdit(self.upload_tab)
        self.url_of_exe_box.setGeometry(QtCore.QRect(10, 195, 291, 31))
        self.url_of_exe_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                          "border-radius: 5px;    \n"
                                          "color: rgb(242, 242, 242);")
        self.url_of_exe_box.setObjectName("url_of_exe_box")
        self.source_url_box = QtWidgets.QLineEdit(self.upload_tab)
        self.source_url_box.setGeometry(QtCore.QRect(10, 230, 291, 31))
        self.source_url_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                          "border-radius: 5px;    \n"
                                          "color: rgb(242, 242, 242);")
        self.source_url_box.setObjectName("source_url_box")
        self.dependency_url_box = QtWidgets.QLineEdit(self.upload_tab)
        self.dependency_url_box.setGeometry(QtCore.QRect(10, 265, 291, 31))
        self.dependency_url_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                              "border-radius: 5px;    \n"
                                              "color: rgb(242, 242, 242);")
        self.dependency_url_box.setObjectName("dependency_url_box")
        self.dependency_run_box = QtWidgets.QLineEdit(self.upload_tab)
        self.dependency_run_box.setGeometry(QtCore.QRect(10, 300, 291, 31))
        self.dependency_run_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                              "border-radius: 5px;    \n"
                                              "color: rgb(242, 242, 242);")
        self.dependency_run_box.setObjectName("dependency_run_box")
        self.main_exe_box = QtWidgets.QLineEdit(self.upload_tab)
        self.main_exe_box.setGeometry(QtCore.QRect(10, 335, 291, 31))
        self.main_exe_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                        "border-radius: 5px;    \n"
                                        "color: rgb(242, 242, 242);")
        self.main_exe_box.setObjectName("main_exe_box")
        self.upload_button = QtWidgets.QPushButton(self.upload_tab)
        self.upload_button.setEnabled(True)
        self.upload_button.setGeometry(QtCore.QRect(10, 380, 291, 50))
        self.upload_button.setMinimumSize(QtCore.QSize(0, 50))
        self.upload_button.setStyleSheet("QPushButton {\n"
                                         "    color: rgb(204, 204, 204);\n"
                                         "    border-width: 1px;\n"
                                         "    border-radius:6px;\n"
                                         "    border-style: solid;\n"
                                         "    background-color: rgb(28, 30, 33);\n"
                                         "    border-color: rgb(66, 143, 225);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border-width: 2px;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: rgb(50, 60, 63);\n"
                                         "}\n"
                                         "QPushButton:disabled{\n"
                                         "    border-width: 0px;\n"
                                         "    background-color: rgb(92, 99, 109);\n"
                                         "}")
        self.upload_button.setObjectName("upload_button")
        self.safetywarning_message = QtWidgets.QTextBrowser(self.upload_tab)
        self.safetywarning_message.setGeometry(QtCore.QRect(10, 450, 281, 161))
        self.safetywarning_message.setStyleSheet("color: white;\n"
                                                 "border: none;")
        self.safetywarning_message.setAcceptRichText(False)
        self.safetywarning_message.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.safetywarning_message.setObjectName("safetywarning_message")
        self.horsy_logo_big = QtWidgets.QLabel(self.upload_tab)
        self.horsy_logo_big.setGeometry(QtCore.QRect(390, 40, 471, 551))
        self.horsy_logo_big.setStyleSheet("background: none")
        self.horsy_logo_big.setText("")
        self.horsy_logo_big.setPixmap(QtGui.QPixmap(":/images/horsy_white.png"))
        self.horsy_logo_big.setObjectName("horsy_logo_big")
        self.tabWidget.addTab(self.upload_tab, "")
        self.browse_tab = QtWidgets.QWidget()
        self.browse_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.browse_tab.setObjectName("browse_tab")
        self.search_table = QtWidgets.QTableWidget(self.browse_tab)
        self.search_table.setGeometry(QtCore.QRect(0, 90, 871, 481))
        self.search_table.setStyleSheet("QTableWidget\n"
                                        "{\n"
                                        "color: white;\n"
                                        "font: 15pt \"MS Shell Dlg 2\";\n"
                                        "margin: 20px;\n"
                                        "border-radius: 45px;\n"
                                        "}\n"
                                        "")
        self.search_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.search_table.setAutoScroll(False)
        self.search_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.search_table.setTabKeyNavigation(False)
        self.search_table.setProperty("showDropIndicator", False)
        self.search_table.setDragDropOverwriteMode(False)
        self.search_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.search_table.setShowGrid(False)
        self.search_table.setObjectName("search_table")
        self.search_table.horizontalHeader().setVisible(False)
        self.search_table.horizontalHeader().setDefaultSectionSize(203)
        self.search_table.horizontalHeader().setHighlightSections(False)
        self.search_table.horizontalHeader().setMinimumSectionSize(150)
        self.search_table.verticalHeader().setVisible(False)
        self.search_table.verticalHeader().setDefaultSectionSize(120)
        self.search_table.verticalHeader().setHighlightSections(False)
        self.search_box = QtWidgets.QTextEdit(self.browse_tab)
        self.search_box.setEnabled(True)
        self.search_box.setGeometry(QtCore.QRect(30, 30, 711, 51))
        self.search_box.setStyleSheet("QTextEdit {\n"
                                      "    background-color: rgb(74, 76, 83);\n"
                                      "    border-radius: 15px;    \n"
                                      "    color: rgb(242, 242, 242);\n"
                                      "    padding: 15px, 15px;\n"
                                      "    border: 15px white;\n"
                                      "}")
        self.search_box.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.search_box.setAcceptRichText(False)
        self.search_box.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.search_box.setObjectName("search_box")
        self.search_button = QtWidgets.QPushButton(self.browse_tab)
        self.search_button.setEnabled(True)
        self.search_button.setGeometry(QtCore.QRect(750, 30, 91, 50))
        self.search_button.setMinimumSize(QtCore.QSize(0, 50))
        self.search_button.setStyleSheet("QPushButton {\n"
                                         "    color: rgb(204, 204, 204);\n"
                                         "    border-width: 1px;\n"
                                         "    border-radius:6px;\n"
                                         "    border-style: solid;\n"
                                         "    background-color: rgb(28, 30, 33);\n"
                                         "    border-color: rgb(66, 143, 225);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border-width: 2px;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: rgb(50, 60, 63);\n"
                                         "}\n"
                                         "QPushButton:disabled{\n"
                                         "    border-width: 0px;\n"
                                         "    background-color: rgb(92, 99, 109);\n"
                                         "}")
        self.search_button.setObjectName("search_button")
        self.install_button = QtWidgets.QPushButton(self.browse_tab)
        self.install_button.setEnabled(True)
        self.install_button.setGeometry(QtCore.QRect(20, 575, 146, 50))
        self.install_button.setMinimumSize(QtCore.QSize(0, 50))
        self.install_button.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(204, 204, 204);\n"
                                          "    border-width: 1px;\n"
                                          "    border-radius:6px;\n"
                                          "    border-style: solid;\n"
                                          "    background-color: rgb(28, 30, 33);\n"
                                          "    border-color: rgb(66, 143, 225);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    border-width: 2px;\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "    background-color: rgb(50, 60, 63);\n"
                                          "}\n"
                                          "QPushButton:disabled{\n"
                                          "    border-width: 0px;\n"
                                          "    background-color: rgb(92, 99, 109);\n"
                                          "}")
        self.install_button.setObjectName("install_button")
        self.source_button = QtWidgets.QPushButton(self.browse_tab)
        self.source_button.setEnabled(True)
        self.source_button.setGeometry(QtCore.QRect(190, 575, 146, 50))
        self.source_button.setMinimumSize(QtCore.QSize(0, 50))
        self.source_button.setStyleSheet("QPushButton {\n"
                                         "    color: rgb(204, 204, 204);\n"
                                         "    border-width: 1px;\n"
                                         "    border-radius:6px;\n"
                                         "    border-style: solid;\n"
                                         "    background-color: rgb(28, 30, 33);\n"
                                         "    border-color: rgb(66, 143, 225);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border-width: 2px;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: rgb(50, 60, 63);\n"
                                         "}\n"
                                         "QPushButton:disabled{\n"
                                         "    border-width: 0px;\n"
                                         "    background-color: rgb(92, 99, 109);\n"
                                         "}")
        self.source_button.setObjectName("source_button")
        self.info_button = QtWidgets.QPushButton(self.browse_tab)
        self.info_button.setEnabled(True)
        self.info_button.setGeometry(QtCore.QRect(360, 575, 146, 50))
        self.info_button.setMinimumSize(QtCore.QSize(0, 50))
        self.info_button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(204, 204, 204);\n"
                                       "    border-width: 1px;\n"
                                       "    border-radius:6px;\n"
                                       "    border-style: solid;\n"
                                       "    background-color: rgb(28, 30, 33);\n"
                                       "    border-color: rgb(66, 143, 225);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    border-width: 2px;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgb(50, 60, 63);\n"
                                       "}\n"
                                       "QPushButton:disabled{\n"
                                       "    border-width: 0px;\n"
                                       "    background-color: rgb(92, 99, 109);\n"
                                       "}")
        self.info_button.setObjectName("info_button")
        self.like_button = QtWidgets.QPushButton(self.browse_tab)
        self.like_button.setEnabled(True)
        self.like_button.setGeometry(QtCore.QRect(540, 575, 146, 50))
        self.like_button.setMinimumSize(QtCore.QSize(0, 50))
        self.like_button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(204, 204, 204);\n"
                                       "    border-width: 1px;\n"
                                       "    border-radius:6px;\n"
                                       "    border-style: solid;\n"
                                       "    background-color: rgb(28, 30, 33);\n"
                                       "    border-color: rgb(66, 143, 225);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    border-width: 2px;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgb(50, 60, 63);\n"
                                       "}\n"
                                       "QPushButton:disabled{\n"
                                       "    border-width: 0px;\n"
                                       "    background-color: rgb(92, 99, 109);\n"
                                       "}")
        self.like_button.setObjectName("like_button")
        self.dislike_button = QtWidgets.QPushButton(self.browse_tab)
        self.dislike_button.setEnabled(True)
        self.dislike_button.setGeometry(QtCore.QRect(710, 575, 146, 50))
        self.dislike_button.setMinimumSize(QtCore.QSize(0, 50))
        self.dislike_button.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(204, 204, 204);\n"
                                          "    border-width: 1px;\n"
                                          "    border-radius:6px;\n"
                                          "    border-style: solid;\n"
                                          "    background-color: rgb(28, 30, 33);\n"
                                          "    border-color: rgb(66, 143, 225);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    border-width: 2px;\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "    background-color: rgb(50, 60, 63);\n"
                                          "}\n"
                                          "QPushButton:disabled{\n"
                                          "    border-width: 0px;\n"
                                          "    background-color: rgb(92, 99, 109);\n"
                                          "}")
        self.dislike_button.setObjectName("dislike_button")
        self.algolia_logo = QtWidgets.QLabel(self.browse_tab)
        self.algolia_logo.setGeometry(QtCore.QRect(820, 530, 31, 31))
        self.algolia_logo.setStyleSheet("background: none;")
        self.algolia_logo.setText("")
        self.algolia_logo.setPixmap(QtGui.QPixmap(":/images/algolia120x32.png"))
        self.algolia_logo.setObjectName("algolia_logo")
        self.tabWidget.addTab(self.browse_tab, "")
        self.installed_tab = QtWidgets.QWidget()
        self.installed_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.installed_tab.setObjectName("installed_tab")
        self.delete_button = QtWidgets.QPushButton(self.installed_tab)
        self.delete_button.setEnabled(True)
        self.delete_button.setGeometry(QtCore.QRect(300, 575, 275, 50))
        self.delete_button.setMinimumSize(QtCore.QSize(0, 50))
        self.delete_button.setStyleSheet("QPushButton {\n"
                                         "    color: rgb(204, 204, 204);\n"
                                         "    border-width: 1px;\n"
                                         "    border-radius:6px;\n"
                                         "    border-style: solid;\n"
                                         "    background-color: rgb(28, 30, 33);\n"
                                         "    border-color: rgb(66, 143, 225);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border-width: 2px;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: rgb(50, 60, 63);\n"
                                         "}\n"
                                         "QPushButton:disabled{\n"
                                         "    border-width: 0px;\n"
                                         "    background-color: rgb(92, 99, 109);\n"
                                         "}")
        self.delete_button.setObjectName("delete_button")
        self.update_button = QtWidgets.QPushButton(self.installed_tab)
        self.update_button.setEnabled(True)
        self.update_button.setGeometry(QtCore.QRect(5, 575, 275, 50))
        self.update_button.setMinimumSize(QtCore.QSize(0, 50))
        self.update_button.setStyleSheet("QPushButton {\n"
                                         "    color: rgb(204, 204, 204);\n"
                                         "    border-width: 1px;\n"
                                         "    border-radius:6px;\n"
                                         "    border-style: solid;\n"
                                         "    background-color: rgb(28, 30, 33);\n"
                                         "    border-color: rgb(66, 143, 225);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border-width: 2px;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: rgb(50, 60, 63);\n"
                                         "}\n"
                                         "QPushButton:disabled{\n"
                                         "    border-width: 0px;\n"
                                         "    background-color: rgb(92, 99, 109);\n"
                                         "}")
        self.update_button.setObjectName("update_button")
        self.check_updates_button = QtWidgets.QPushButton(self.installed_tab)
        self.check_updates_button.setEnabled(True)
        self.check_updates_button.setGeometry(QtCore.QRect(595, 575, 275, 50))
        self.check_updates_button.setMinimumSize(QtCore.QSize(0, 50))
        self.check_updates_button.setStyleSheet("QPushButton {\n"
                                                "    color: rgb(204, 204, 204);\n"
                                                "    border-width: 1px;\n"
                                                "    border-radius:6px;\n"
                                                "    border-style: solid;\n"
                                                "    background-color: rgb(28, 30, 33);\n"
                                                "    border-color: rgb(66, 143, 225);\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    border-width: 2px;\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "    background-color: rgb(50, 60, 63);\n"
                                                "}\n"
                                                "QPushButton:disabled{\n"
                                                "    border-width: 0px;\n"
                                                "    background-color: rgb(92, 99, 109);\n"
                                                "}")
        self.check_updates_button.setObjectName("check_updates_button")
        self.installed_table = QtWidgets.QTableWidget(self.installed_tab)
        self.installed_table.setGeometry(QtCore.QRect(0, 10, 871, 571))
        self.installed_table.setStyleSheet("QTableWidget\n"
                                           "{\n"
                                           "color: white;\n"
                                           "font: 15pt \"MS Shell Dlg 2\";\n"
                                           "margin: 20px;\n"
                                           "border-radius: 45px;\n"
                                           "}\n"
                                           "")
        self.installed_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.installed_table.setAutoScroll(False)
        self.installed_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.installed_table.setTabKeyNavigation(False)
        self.installed_table.setProperty("showDropIndicator", False)
        self.installed_table.setDragDropOverwriteMode(False)
        self.installed_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.installed_table.setShowGrid(False)
        self.installed_table.setObjectName("installed_table")
        self.installed_table.horizontalHeader().setVisible(False)
        self.installed_table.horizontalHeader().setDefaultSectionSize(203)
        self.installed_table.horizontalHeader().setHighlightSections(False)
        self.installed_table.horizontalHeader().setMinimumSectionSize(150)
        self.installed_table.verticalHeader().setVisible(False)
        self.installed_table.verticalHeader().setDefaultSectionSize(120)
        self.installed_table.verticalHeader().setHighlightSections(False)
        self.tabWidget.addTab(self.installed_tab, "")
        self.horsy_text_lefttop = QtWidgets.QLabel(self.centralwidget)
        self.horsy_text_lefttop.setGeometry(QtCore.QRect(70, 10, 65, 30))
        self.horsy_text_lefttop.setStyleSheet("color: white;\n"
                                              "font: 20pt \"MS Shell Dlg 2\";\n"
                                              "background: none;")
        self.horsy_text_lefttop.setObjectName("horsy_text_lefttop")
        self.tabWidget.raise_()
        self.horsy_logo_lefttop.raise_()
        self.horsy_text_lefttop.raise_()
        self.requestupdate_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "horsy"))
        self.loginlogout_button.setText(_translate("MainWindow", "Log in/Log out"))
        self.username_box.setPlaceholderText(_translate("MainWindow", "Log in first"))
        self.changeemail_button.setText(_translate("MainWindow", "Change e-mail"))
        self.email_box.setPlaceholderText(_translate("MainWindow", "email"))
        self.oldpass_box.setPlaceholderText(_translate("MainWindow", "Old password"))
        self.newpass_box.setPlaceholderText(_translate("MainWindow", "New password"))
        self.changepass_button.setText(_translate("MainWindow", "Change password"))
        self.manage_packages_table.setSortingEnabled(True)
        __sortingEnabled = self.manage_packages_table.isSortingEnabled()
        self.manage_packages_table.setSortingEnabled(False)
        self.manage_packages_table.setSortingEnabled(__sortingEnabled)
        self.manage_packages_message.setHtml(_translate("MainWindow",
                                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Manage your packages</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account_tab), _translate("MainWindow", "Account"))
        self.packagename_box.setPlaceholderText(_translate("MainWindow", "Package name"))
        self.before_uploading_message.setHtml(_translate("MainWindow",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Before starting, please make sure you have done your project and <span style=\" font-weight:600;\">uploaded</span> it to any hosting service or file sharing service</p></body></html>"))
        self.packagename_message.setHtml(_translate("MainWindow",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It should contain only lowercase letters, underscores and dashes</p></body></html>"))
        self.package_desc_box.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.package_desc_box.setPlaceholderText(
            _translate("MainWindow", "Package description. It should be a short text under 256 characters"))
        self.url_of_exe_box.setPlaceholderText(_translate("MainWindow", "Url of executable (ends on .exe or .zip)"))
        self.source_url_box.setPlaceholderText(
            _translate("MainWindow", "Url of source (project on GitHub, source archive)"))
        self.dependency_url_box.setPlaceholderText(_translate("MainWindow", "Dependency URL (installer in .exe)"))
        self.dependency_run_box.setPlaceholderText(
            _translate("MainWindow", "Dependency run (run this during installation)"))
        self.main_exe_box.setPlaceholderText(
            _translate("MainWindow", "Command ($appdir$\\file.exe, python $appdir$\\main.py, etc)"))
        self.upload_button.setText(_translate("MainWindow", "Upload"))
        self.safetywarning_message.setHtml(_translate("MainWindow",
                                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">We don\'t moderate any apps and we </span><span style=\" font-size:11pt; font-weight:600;\">won\'t</span><span style=\" font-size:11pt;\"> delete your app, if it is not doesn\'t match some rules. But, if your app uses server vulnerabilities or hinders server work, we will delete your app. Keep in mind, that we don\'t responsible for your apps, but we advise you to share only working and safe apps on horsy</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.upload_tab), _translate("MainWindow", "Upload"))
        self.search_table.setSortingEnabled(True)
        __sortingEnabled = self.search_table.isSortingEnabled()
        self.search_table.setSortingEnabled(False)
        self.search_table.setSortingEnabled(__sortingEnabled)
        self.search_box.setPlaceholderText(_translate("MainWindow", "Search packages..."))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.install_button.setText(_translate("MainWindow", "Install"))
        self.source_button.setText(_translate("MainWindow", "Get source"))
        self.info_button.setText(_translate("MainWindow", "Info"))
        self.like_button.setText(_translate("MainWindow", "👍"))
        self.dislike_button.setText(_translate("MainWindow", "👎"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.browse_tab), _translate("MainWindow", "Browse"))
        self.delete_button.setText(_translate("MainWindow", "Uninstall"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.check_updates_button.setText(_translate("MainWindow", "Check all updates"))
        self.installed_table.setSortingEnabled(True)
        __sortingEnabled = self.installed_table.isSortingEnabled()
        self.installed_table.setSortingEnabled(False)
        self.installed_table.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.installed_tab), _translate("MainWindow", "Installed"))
        self.horsy_text_lefttop.setText(_translate("MainWindow", "horsy"))


class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/horsy_white32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.resize(292, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(292, 200))
        MainWindow.setMaximumSize(QtCore.QSize(292, 200))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowOpacity(0.98)
        MainWindow.setStyleSheet("QWidget{\n"
                                 "    background-color: rgb(30, 30, 30);\n"
                                 "}\n"
                                 "")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setEnabled(True)
        self.login_button.setGeometry(QtCore.QRect(70, 140, 151, 50))
        self.login_button.setMinimumSize(QtCore.QSize(0, 50))
        self.login_button.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(204, 204, 204);\n"
                                        "    border-width: 1px;\n"
                                        "    border-radius:6px;\n"
                                        "    border-style: solid;\n"
                                        "    background-color: rgb(28, 30, 33);\n"
                                        "    border-color: rgb(66, 143, 225);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    border-width: 2px;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgb(50, 60, 63);\n"
                                        "}\n"
                                        "QPushButton:disabled{\n"
                                        "    border-width: 0px;\n"
                                        "    background-color: rgb(92, 99, 109);\n"
                                        "}")
        self.login_button.setObjectName("login_button")
        self.email_box = QtWidgets.QLineEdit(self.centralwidget)
        self.email_box.setGeometry(QtCore.QRect(20, 20, 251, 51))
        self.email_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                     "border-radius: 5px;    \n"
                                     "color: rgb(242, 242, 242);")
        self.email_box.setObjectName("email_box")
        self.password_box = QtWidgets.QLineEdit(self.centralwidget)
        self.password_box.setGeometry(QtCore.QRect(20, 80, 251, 51))
        self.password_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                        "border-radius: 5px;    \n"
                                        "color: rgb(242, 242, 242);")
        self.password_box.setInputMask("")
        self.password_box.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_box.setObjectName("password_box")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log in"))
        self.login_button.setText(_translate("MainWindow", "Log in"))
        self.email_box.setPlaceholderText(_translate("MainWindow", "email"))
        self.password_box.setPlaceholderText(_translate("MainWindow", "Password"))


class Ui_DownloadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 252)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/horsy_white32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setMinimumSize(QtCore.QSize(682, 252))
        MainWindow.setMaximumSize(QtCore.QSize(682, 252))
        MainWindow.setStyleSheet("QWidget{\n"
                                 "    background-color: rgb(30, 30, 30);\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logs_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.logs_box.setGeometry(QtCore.QRect(20, 20, 641, 211))
        self.logs_box.setMinimumSize(QtCore.QSize(0, 0))
        self.logs_box.setMaximumSize(QtCore.QSize(1000, 1000))
        self.logs_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                    "border-radius: 5px;    \n"
                                    "color: rgb(242, 242, 242);\n"
                                    'font: 50 12pt "Arial Black";')
        self.logs_box.setAcceptRichText(False)
        self.logs_box.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.logs_box.setObjectName("logs_box")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "horsy"))
        self.logs_box.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.logs_box.setPlaceholderText(_translate("MainWindow", "Logs"))


class Ui_PackageWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/horsy_white32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.resize(331, 433)
        MainWindow.setMinimumSize(QtCore.QSize(331, 433))
        MainWindow.setMaximumSize(QtCore.QSize(331, 433))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "    background-color: rgb(30, 30, 30);\n"
                                         "}\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.packagename_box = QtWidgets.QLineEdit(self.centralwidget)
        self.packagename_box.setGeometry(QtCore.QRect(20, 20, 151, 31))
        self.packagename_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                           "border-radius: 5px;    \n"
                                           "color: rgb(242, 242, 242);")
        self.packagename_box.setText("")
        self.packagename_box.setReadOnly(True)
        self.packagename_box.setObjectName("packagename_box")
        self.main_exe_box = QtWidgets.QLineEdit(self.centralwidget)
        self.main_exe_box.setGeometry(QtCore.QRect(20, 305, 291, 31))
        self.main_exe_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                        "border-radius: 5px;    \n"
                                        "color: rgb(242, 242, 242);")
        self.main_exe_box.setObjectName("main_exe_box")
        self.source_url_box = QtWidgets.QLineEdit(self.centralwidget)
        self.source_url_box.setGeometry(QtCore.QRect(20, 200, 291, 31))
        self.source_url_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                          "border-radius: 5px;    \n"
                                          "color: rgb(242, 242, 242);")
        self.source_url_box.setObjectName("source_url_box")
        self.url_of_exe_box = QtWidgets.QLineEdit(self.centralwidget)
        self.url_of_exe_box.setGeometry(QtCore.QRect(20, 165, 291, 31))
        self.url_of_exe_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                          "border-radius: 5px;    \n"
                                          "color: rgb(242, 242, 242);")
        self.url_of_exe_box.setObjectName("url_of_exe_box")
        self.dependency_url_box = QtWidgets.QLineEdit(self.centralwidget)
        self.dependency_url_box.setGeometry(QtCore.QRect(20, 235, 291, 31))
        self.dependency_url_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                              "border-radius: 5px;    \n"
                                              "color: rgb(242, 242, 242);")
        self.dependency_url_box.setObjectName("dependency_url_box")
        self.dependency_run_box = QtWidgets.QLineEdit(self.centralwidget)
        self.dependency_run_box.setGeometry(QtCore.QRect(20, 270, 291, 31))
        self.dependency_run_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                              "border-radius: 5px;    \n"
                                              "color: rgb(242, 242, 242);")
        self.dependency_run_box.setObjectName("dependency_run_box")
        self.package_desc_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.package_desc_box.setGeometry(QtCore.QRect(20, 60, 256, 101))
        self.package_desc_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                            "border-radius: 5px;    \n"
                                            "color: rgb(242, 242, 242);")
        self.package_desc_box.setAcceptRichText(False)
        self.package_desc_box.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.package_desc_box.setObjectName("package_desc_box")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setEnabled(True)
        self.update_button.setGeometry(QtCore.QRect(20, 360, 291, 50))
        self.update_button.setMinimumSize(QtCore.QSize(0, 50))
        self.update_button.setStyleSheet("QPushButton {\n"
                                         "    color: rgb(204, 204, 204);\n"
                                         "    border-width: 1px;\n"
                                         "    border-radius:6px;\n"
                                         "    border-style: solid;\n"
                                         "    background-color: rgb(28, 30, 33);\n"
                                         "    border-color: rgb(66, 143, 225);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    border-width: 2px;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: rgb(50, 60, 63);\n"
                                         "}\n"
                                         "QPushButton:disabled{\n"
                                         "    border-width: 0px;\n"
                                         "    background-color: rgb(92, 99, 109);\n"
                                         "}")
        self.update_button.setObjectName("update_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "horsy - editing package"))
        self.packagename_box.setPlaceholderText(_translate("MainWindow", "Editing package"))
        self.main_exe_box.setPlaceholderText(
            _translate("MainWindow", "Main executable command ($appdir$\\file.exe, python $appdir$\\main.py, etc)"))
        self.source_url_box.setPlaceholderText(
            _translate("MainWindow", "Url of source (project on GitHub, source archive)"))
        self.url_of_exe_box.setPlaceholderText(_translate("MainWindow", "Url of executable (ends on .exe or .zip)"))
        self.dependency_url_box.setPlaceholderText(_translate("MainWindow", "Dependency URL (installer in .exe)"))
        self.dependency_run_box.setPlaceholderText(
            _translate("MainWindow", "Dependency run (run this during installation)"))
        self.package_desc_box.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.package_desc_box.setPlaceholderText(
            _translate("MainWindow", "Package description. It should be a short text under 256 characters"))
        self.update_button.setText(_translate("MainWindow", "Update"))


def popup(title, text):
    QtWidgets.QMessageBox.information(None, title, text)


def cpopup(title, text, style=0):
    """
    Styles:
    0 : OK
    1 : OK | Cancel
    2 : Abort | Retry | Ignore
    3 : Yes | No | Cancel
    4 : Yes | No
    5 : Retry | Cancel
    6 : Cancel | Try Again | Continue
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
