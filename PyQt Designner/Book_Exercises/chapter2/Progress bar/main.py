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
        Dialog.resize(452, 306)
        self.progress = QtWidgets.QProgressBar(Dialog)
        self.progress.setGeometry(QtCore.QRect(60, 140, 311, 23))
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 100, 141, 17))
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(130, 190, 171, 61))
        self.start.setObjectName("start")
        self.time = QtWidgets.QLineEdit(Dialog)
        self.time.setGeometry(QtCore.QRect(300, 50, 113, 25))
        self.time.setText("")
        self.time.setObjectName("time")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 67, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.start.clicked.connect(Dialog.start_download)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading ..."))
        self.start.setText(_translate("Dialog", "Start Download"))
        self.label_2.setText(_translate("Dialog", "Time"))
