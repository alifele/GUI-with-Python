# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 250, 67, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 51, 114, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.small_radio = QtWidgets.QRadioButton(self.widget)
        self.small_radio.setObjectName("small_radio")
        self.verticalLayout.addWidget(self.small_radio)
        self.medium_radio = QtWidgets.QRadioButton(self.widget)
        self.medium_radio.setObjectName("medium_radio")
        self.verticalLayout.addWidget(self.medium_radio)
        self.large_radio = QtWidgets.QRadioButton(self.widget)
        self.large_radio.setObjectName("large_radio")
        self.verticalLayout.addWidget(self.large_radio)
        self.xlarge_radio = QtWidgets.QRadioButton(self.widget)
        self.xlarge_radio.setObjectName("xlarge_radio")
        self.verticalLayout.addWidget(self.xlarge_radio)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(270, 50, 94, 101))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cheeese_option = QtWidgets.QCheckBox(self.widget1)
        self.cheeese_option.setObjectName("cheeese_option")
        self.verticalLayout_2.addWidget(self.cheeese_option)
        self.olive_option = QtWidgets.QCheckBox(self.widget1)
        self.olive_option.setObjectName("olive_option")
        self.verticalLayout_2.addWidget(self.olive_option)
        self.peperoption = QtWidgets.QCheckBox(self.widget1)
        self.peperoption.setObjectName("peperoption")
        self.verticalLayout_2.addWidget(self.peperoption)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(100, 240, 196, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.calculate = QtWidgets.QPushButton(self.splitter)
        self.calculate.setObjectName("calculate")
        self.price_label = QtWidgets.QLabel(self.splitter)
        self.price_label.setObjectName("price_label")

        self.retranslateUi(Dialog)
        self.small_radio.toggled['bool'].connect(Dialog.update_val)
        self.medium_radio.toggled['bool'].connect(Dialog.update_val)
        self.large_radio.toggled['bool'].connect(Dialog.update_val)
        self.xlarge_radio.toggled['bool'].connect(Dialog.update_val)
        self.cheeese_option.toggled['bool'].connect(Dialog.incval)
        self.olive_option.toggled['bool'].connect(Dialog.incval)
        self.peperoption.toggled['bool'].connect(Dialog.incval)
        self.calculate.clicked['bool'].connect(Dialog.showcal)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.small_radio.setText(_translate("Dialog", "small"))
        self.medium_radio.setText(_translate("Dialog", "medium"))
        self.large_radio.setText(_translate("Dialog", "large"))
        self.xlarge_radio.setText(_translate("Dialog", "x Large"))
        self.cheeese_option.setText(_translate("Dialog", "X cheese"))
        self.olive_option.setText(_translate("Dialog", "X olive"))
        self.peperoption.setText(_translate("Dialog", "X peper"))
        self.calculate.setText(_translate("Dialog", "Calculate"))
        self.price_label.setText(_translate("Dialog", "select ..."))
