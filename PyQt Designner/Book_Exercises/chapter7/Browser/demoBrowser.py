# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 67, 17))
        self.label.setObjectName("label")
        self.lineEditURL = QtWidgets.QLineEdit(Dialog)
        self.lineEditURL.setGeometry(QtCore.QRect(30, 30, 261, 25))
        self.lineEditURL.setObjectName("lineEditURL")
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        self.pushButtonGo.setGeometry(QtCore.QRect(300, 30, 89, 25))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.widget = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 80, 351, 201))
        self.widget.setObjectName("widget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter URL"))
        self.pushButtonGo.setText(_translate("Dialog", "GO"))
#from PyQt5 import QtWebEngineWidgets
