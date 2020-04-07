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
        Dialog.resize(548, 300)
        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setGeometry(QtCore.QRect(30, 40, 201, 25))
        self.input_name.setObjectName("input_name")
        self.Add = QtWidgets.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(30, 100, 89, 25))
        self.Add.setObjectName("Add")
        self.List = QtWidgets.QListWidget(Dialog)
        self.List.setGeometry(QtCore.QRect(270, 40, 256, 192))
        self.List.setObjectName("List")
        self.Edit = QtWidgets.QPushButton(Dialog)
        self.Edit.setGeometry(QtCore.QRect(270, 250, 61, 25))
        self.Edit.setObjectName("Edit")
        self.Delete = QtWidgets.QPushButton(Dialog)
        self.Delete.setGeometry(QtCore.QRect(360, 250, 61, 25))
        self.Delete.setObjectName("Delete")
        self.DeleteAll = QtWidgets.QPushButton(Dialog)
        self.DeleteAll.setGeometry(QtCore.QRect(440, 250, 81, 25))
        self.DeleteAll.setObjectName("DeleteAll")

        self.retranslateUi(Dialog)
        self.Add.clicked.connect(Dialog.add_to_list)
        self.Delete.clicked.connect(Dialog.del_list)
        self.Edit.clicked.connect(Dialog.edit_list)
        self.DeleteAll.clicked.connect(Dialog.delete_all)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Add.setText(_translate("Dialog", "Add to List"))
        self.Edit.setText(_translate("Dialog", "Edit"))
        self.Delete.setText(_translate("Dialog", "Delete"))
        self.DeleteAll.setText(_translate("Dialog", "Delete All"))
