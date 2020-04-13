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
        Dialog.resize(400, 242)
        self.calculate_button = QtWidgets.QPushButton(Dialog)
        self.calculate_button.setGeometry(QtCore.QRect(300, 120, 89, 51))
        self.calculate_button.setObjectName("calculate_button")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 281, 211))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.code_enter = QtWidgets.QLineEdit(self.widget)
        self.code_enter.setObjectName("code_enter")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.code_enter)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name_enter = QtWidgets.QLineEdit(self.widget)
        self.name_enter.setObjectName("name_enter")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_enter)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.geo_enter = QtWidgets.QLineEdit(self.widget)
        self.geo_enter.setObjectName("geo_enter")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.geo_enter)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.his_enter = QtWidgets.QLineEdit(self.widget)
        self.his_enter.setObjectName("his_enter")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.his_enter)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.total_show = QtWidgets.QLineEdit(self.widget)
        self.total_show.setReadOnly(True)
        self.total_show.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.total_show.setObjectName("total_show")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.total_show)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.average_show = QtWidgets.QLineEdit(self.widget)
        self.average_show.setReadOnly(True)
        self.average_show.setObjectName("average_show")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.average_show)

        self.retranslateUi(Dialog)
        self.calculate_button.clicked.connect(Dialog.compute_button)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.calculate_button.setText(_translate("Dialog", "Calculate"))
        self.label.setText(_translate("Dialog", "Code"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Geo"))
        self.label_4.setText(_translate("Dialog", "History"))
        self.label_5.setText(_translate("Dialog", "Total"))
        self.label_6.setText(_translate("Dialog", "Average"))
