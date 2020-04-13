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
        Dialog.resize(732, 359)
        self.button_show = QtWidgets.QPushButton(Dialog)
        self.button_show.setGeometry(QtCore.QRect(40, 180, 89, 25))
        self.button_show.setObjectName("button_show")
        self.lable_show = QtWidgets.QLabel(Dialog)
        self.lable_show.setGeometry(QtCore.QRect(50, 100, 141, 51))
        self.lable_show.setObjectName("lable_show")
        self.name_enter = QtWidgets.QLineEdit(Dialog)
        self.name_enter.setGeometry(QtCore.QRect(30, 40, 271, 25))
        self.name_enter.setObjectName("name_enter")
        self.names_list = QtWidgets.QListWidget(Dialog)
        self.names_list.setGeometry(QtCore.QRect(350, 40, 256, 192))
        self.names_list.setObjectName("names_list")
        self.update_list = QtWidgets.QPushButton(Dialog)
        self.update_list.setGeometry(QtCore.QRect(430, 270, 89, 25))
        self.update_list.setObjectName("update_list")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_show.setText(_translate("Dialog", "Show Name"))
        self.lable_show.setText(_translate("Dialog", "TextLabel"))
        self.update_list.setText(_translate("Dialog", "Update List"))
