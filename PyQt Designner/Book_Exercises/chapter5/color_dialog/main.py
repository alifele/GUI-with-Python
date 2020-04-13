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
        self.color_frame = QtWidgets.QFrame(Dialog)
        self.color_frame.setGeometry(QtCore.QRect(240, 50, 120, 80))
        self.color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_frame.setObjectName("color_frame")
        self.show_color_dialog = QtWidgets.QPushButton(Dialog)
        self.show_color_dialog.setGeometry(QtCore.QRect(20, 110, 89, 25))
        self.show_color_dialog.setObjectName("show_color_dialog")
        self.color_label = QtWidgets.QLabel(Dialog)
        self.color_label.setGeometry(QtCore.QRect(250, 160, 67, 17))
        self.color_label.setObjectName("color_label")

        self.retranslateUi(Dialog)
        self.show_color_dialog.clicked.connect(Dialog.show_color_dialog_F)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.show_color_dialog.setText(_translate("Dialog", "Select Color"))
        self.color_label.setText(_translate("Dialog", "TextLabel"))
