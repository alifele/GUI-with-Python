# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.TEXT = QtWidgets.QTextEdit(Dialog)
        self.TEXT.setGeometry(QtCore.QRect(100, 30, 241, 151))
        self.TEXT.setObjectName("TEXT")
        self.change_font_button = QtWidgets.QPushButton(Dialog)
        self.change_font_button.setGeometry(QtCore.QRect(160, 210, 131, 51))
        self.change_font_button.setObjectName("change_font_button")

        self.retranslateUi(Dialog)
        self.change_font_button.clicked.connect(Dialog.open_font_dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.change_font_button.setText(_translate("Dialog", "Change Font"))
