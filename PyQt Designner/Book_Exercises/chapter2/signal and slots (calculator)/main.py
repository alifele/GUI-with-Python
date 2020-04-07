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
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 217, 58))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.input1 = QtWidgets.QLineEdit(self.widget)
        self.input1.setObjectName("input1")
        self.gridLayout_2.addWidget(self.input1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.input2 = QtWidgets.QLineEdit(self.widget)
        self.input2.setObjectName("input2")
        self.gridLayout_2.addWidget(self.input2, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(30, 100, 232, 83))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.add = QtWidgets.QRadioButton(self.widget1)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 0, 0, 1, 1)
        self.dev = QtWidgets.QRadioButton(self.widget1)
        self.dev.setObjectName("dev")
        self.gridLayout.addWidget(self.dev, 2, 1, 1, 1)
        self.sub = QtWidgets.QRadioButton(self.widget1)
        self.sub.setObjectName("sub")
        self.gridLayout.addWidget(self.sub, 2, 0, 1, 1)
        self.mult = QtWidgets.QRadioButton(self.widget1)
        self.mult.setObjectName("mult")
        self.gridLayout.addWidget(self.mult, 0, 1, 1, 1)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(50, 210, 261, 81))
        self.widget2.setObjectName("widget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)
        self.cal = QtWidgets.QPushButton(self.widget2)
        self.cal.setObjectName("cal")
        self.gridLayout_3.addWidget(self.cal, 1, 0, 1, 1)
        self.result = QtWidgets.QLabel(self.widget2)
        self.result.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout_3.addWidget(self.result, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.add.toggled['bool'].connect(Dialog.add)
        self.sub.toggled['bool'].connect(Dialog.sub)
        self.dev.toggled['bool'].connect(Dialog.dev)
        self.mult.toggled['bool'].connect(Dialog.mult)
        self.cal.clicked['bool'].connect(Dialog.show_cal)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input_1"))
        self.label_2.setText(_translate("Dialog", "Input_2"))
        self.add.setText(_translate("Dialog", "Add"))
        self.dev.setText(_translate("Dialog", "Devide"))
        self.sub.setText(_translate("Dialog", "Subtract"))
        self.mult.setText(_translate("Dialog", "Multiply"))
        self.label_4.setText(_translate("Dialog", "Result:"))
        self.cal.setText(_translate("Dialog", "Calculate"))
