# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.copy = QtWidgets.QPushButton(Dialog)
        self.copy.setGeometry(QtCore.QRect(40, 170, 89, 25))
        self.copy.setObjectName("copy")
        self.enter = QtWidgets.QLineEdit(Dialog)
        self.enter.setGeometry(QtCore.QRect(50, 70, 113, 25))
        self.enter.setObjectName("enter")
        self.paste = QtWidgets.QPushButton(Dialog)
        self.paste.setGeometry(QtCore.QRect(260, 160, 89, 25))
        self.paste.setObjectName("paste")
        self.output = QtWidgets.QLineEdit(Dialog)
        self.output.setGeometry(QtCore.QRect(240, 70, 113, 25))
        self.output.setObjectName("output")

        self.retranslateUi(Dialog)
        self.copy.pressed.connect(self.enter.selectAll)
        self.paste.clicked.connect(self.output.paste)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.copy.setText(_translate("Dialog", "Copy"))
        self.paste.setText(_translate("Dialog", "Paste"))
