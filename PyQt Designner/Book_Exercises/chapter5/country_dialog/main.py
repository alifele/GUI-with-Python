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
        Dialog.resize(574, 253)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(36, 10, 501, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.name_enter = QtWidgets.QLineEdit(self.widget)
        self.name_enter.setObjectName("name_enter")
        self.gridLayout.addWidget(self.name_enter, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.age_enter = QtWidgets.QLineEdit(self.widget)
        self.age_enter.setObjectName("age_enter")
        self.gridLayout.addWidget(self.age_enter, 1, 1, 1, 1)
        self.open_age_dialog = QtWidgets.QPushButton(self.widget)
        self.open_age_dialog.setObjectName("open_age_dialog")
        self.gridLayout.addWidget(self.open_age_dialog, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.weight_enter = QtWidgets.QLineEdit(self.widget)
        self.weight_enter.setObjectName("weight_enter")
        self.gridLayout.addWidget(self.weight_enter, 2, 1, 1, 1)
        self.open_weight_dialog = QtWidgets.QPushButton(self.widget)
        self.open_weight_dialog.setObjectName("open_weight_dialog")
        self.gridLayout.addWidget(self.open_weight_dialog, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.country_enetr = QtWidgets.QLineEdit(self.widget)
        self.country_enetr.setObjectName("country_enetr")
        self.gridLayout.addWidget(self.country_enetr, 3, 1, 1, 1)
        self.open_country_dialog = QtWidgets.QPushButton(self.widget)
        self.open_country_dialog.setObjectName("open_country_dialog")
        self.gridLayout.addWidget(self.open_country_dialog, 3, 2, 1, 1)
        self.open_name_dialog = QtWidgets.QPushButton(self.widget)
        self.open_name_dialog.setObjectName("open_name_dialog")
        self.gridLayout.addWidget(self.open_name_dialog, 0, 2, 1, 1)

        self.country_enetr.setReadOnly(True)
        self.name_enter.setReadOnly(True)
        self.age_enter.setReadOnly(True)
        self.weight_enter.setReadOnly(True)

        self.retranslateUi(Dialog)
        self.open_name_dialog.clicked.connect(Dialog.open_name_dialog_F)
        self.open_age_dialog.clicked.connect(Dialog.open_age_dialog_F)
        self.open_weight_dialog.clicked.connect(Dialog.open_weight_dialog_F)
        self.open_country_dialog.clicked.connect(Dialog.open_country_dialog_F)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "your Name"))
        self.label_3.setText(_translate("Dialog", "your Age"))
        self.open_age_dialog.setText(_translate("Dialog", "select ..."))
        self.label.setText(_translate("Dialog", "your weight"))
        self.open_weight_dialog.setText(_translate("Dialog", "select ..."))
        self.label_2.setText(_translate("Dialog", "your country"))
        self.open_country_dialog.setText(_translate("Dialog", "select ..."))
        self.open_name_dialog.setText(_translate("Dialog", "select ..."))
