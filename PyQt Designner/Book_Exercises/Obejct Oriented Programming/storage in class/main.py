# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, MName):

        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 281)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 130, 231, 61))
        self.pushButton.setObjectName("pushButton")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(90, 90, 291, 21))
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 60, 171, 17))
        self.label.setObjectName("label")


        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(MName.show_dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Show"))
        self.label.setText(_translate("Dialog", "Enter you name"))
