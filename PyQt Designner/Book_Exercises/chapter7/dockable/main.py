# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sign_dock = QtWidgets.QDockWidget(MainWindow)
        self.sign_dock.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.sign_dock.setFloating(False)
        self.sign_dock.setObjectName("sign_dock")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.email_lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.email_lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 25))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.pass_lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.pass_lineEdit.setGeometry(QtCore.QRect(130, 120, 113, 25))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 111, 17))
        self.label_2.setObjectName("label_2")
        self.show_button = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.show_button.setGeometry(QtCore.QRect(60, 200, 89, 25))
        self.show_button.setObjectName("show_button")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_3.setGeometry(QtCore.QRect(70, 330, 121, 31))
        self.label_3.setObjectName("label_3")
        self.email_pass_label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.email_pass_label.setGeometry(QtCore.QRect(70, 370, 111, 111))
        self.email_pass_label.setTextFormat(QtCore.Qt.RichText)
        self.email_pass_label.setObjectName("email_pass_label")
        self.sign_dock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.sign_dock)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sign_dock.setWindowTitle(_translate("MainWindow", "The Sign in Window"))
        self.label.setText(_translate("MainWindow", "Your Email"))
        self.label_2.setText(_translate("MainWindow", "Your password"))
        self.show_button.setText(_translate("MainWindow", "Show"))
        self.label_3.setText(_translate("MainWindow", "email_password"))
        self.email_pass_label.setText(_translate("MainWindow", "TextLabel"))
