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
        self.items = QtWidgets.QComboBox(Dialog)
        self.items.setGeometry(QtCore.QRect(30, 60, 251, 25))
        self.items.setObjectName("items")
        self.items.addItem('Hello')
        self.items.addItem('There')
        self.items.addItem('Ali')
        self.items.addItem('Fele')
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 181, 17))
        self.label.setObjectName("label")
        self.buttom_result = QtWidgets.QLabel(Dialog)
        self.buttom_result.setGeometry(QtCore.QRect(50, 200, 101, 61))
        self.buttom_result.setObjectName("buttom_result")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 120, 101, 61))
        self.pushButton.setObjectName("pushButton")
        self.action_result = QtWidgets.QLabel(Dialog)
        self.action_result.setGeometry(QtCore.QRect(220, 190, 151, 91))
        self.action_result.setObjectName("action_result")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 160, 111, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.items.highlighted['QString'].connect(Dialog.action_update)
        #self.items.activated['QString'].connect(Dialog.action_update)
        #self.items.currentIndexChanged['QString'].connect(Dialog.action_update)
        self.pushButton.clicked.connect(Dialog.Show_update)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select one Item"))
        self.buttom_result.setText(_translate("Dialog", "Press Show..."))
        self.pushButton.setText(_translate("Dialog", "Show"))
        self.action_result.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "action_result"))
