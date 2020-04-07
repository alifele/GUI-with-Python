# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label_response = QtWidgets.QLabel(Dialog)
        self.label_response.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.label_response.setObjectName("label_response")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(210, 20, 181, 25))
        self.lineEditName.setObjectName("lineEditName")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 80, 191, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 190, 67, 17))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_response.setText(_translate("Dialog", "Please Enetr Your Name"))
        self.pushButton.setText(_translate("Dialog", "Click!"))
        self.label.setText(_translate("Dialog", "TextLabel"))
