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
        Dialog.resize(584, 337)
        self.show_button = QtWidgets.QPushButton(Dialog)
        self.show_button.setGeometry(QtCore.QRect(100, 270, 121, 51))
        self.show_button.setObjectName("show_button")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(360, 160, 67, 17))
        self.label_5.setObjectName("label_5")
        self.TEXTs = QtWidgets.QLabel(Dialog)
        self.TEXTs.setGeometry(QtCore.QRect(370, 190, 171, 111))
        self.TEXTs.setObjectName("TEXTs")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(11, 22, 311, 231))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.code_enter = QtWidgets.QLineEdit(self.widget)
        self.code_enter.setObjectName("code_enter")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.code_enter)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name_enter = QtWidgets.QLineEdit(self.widget)
        self.name_enter.setObjectName("name_enter")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.name_enter)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.history_enter = QtWidgets.QLineEdit(self.widget)
        self.history_enter.setObjectName("history_enter")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.history_enter)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Geo_enter = QtWidgets.QLineEdit(self.widget)
        self.Geo_enter.setObjectName("Geo_enter")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Geo_enter)

        self.retranslateUi(Dialog)
        self.show_button.clicked.connect(Dialog.update_text)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.show_button.setText(_translate("Dialog", "Show"))
        self.label_5.setText(_translate("Dialog", "Marks"))
        self.TEXTs.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "Code"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "History Mark"))
        self.label_4.setText(_translate("Dialog", "Geo Mark"))
