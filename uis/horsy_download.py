# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\RAZNOE\prgrming\horsy\Source\client\uis\horsy_download.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 252)
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
"color: rgb(242, 242, 242);")
        self.logs_box.setAcceptRichText(False)
        self.logs_box.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logs_box.setObjectName("logs_box")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloading"))
        self.logs_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.logs_box.setPlaceholderText(_translate("MainWindow", "Logs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())