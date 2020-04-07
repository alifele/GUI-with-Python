# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from myimports import * 


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.font_list = QtWidgets.QFontComboBox(Dialog)
        self.font_list.setGeometry(QtCore.QRect(30, 70, 244, 25))
        self.font_list.setObjectName("font_list")
        self.textBrowser = QtWidgets.QPlainTextEdit(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(100, 120, 231, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 130, 51, 91))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 27, 161, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.font_list.activated['QString'].connect(Dialog.UpdateText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Enter </p><p>Your </p><p>Text</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Select one Font"))
