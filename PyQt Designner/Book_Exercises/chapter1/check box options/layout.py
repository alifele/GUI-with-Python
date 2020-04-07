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
        Dialog.resize(400, 371)
        self.calculate_button = QtWidgets.QPushButton(Dialog)
        self.calculate_button.setGeometry(QtCore.QRect(28, 250, 111, 81))
        self.calculate_button.setObjectName("calculate_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 250, 67, 17))
        self.label.setObjectName("label")
        self.price_label = QtWidgets.QLabel(Dialog)
        self.price_label.setGeometry(QtCore.QRect(210, 280, 151, 51))
        self.price_label.setStyleSheet("background-color: rgb(163, 191, 207);")
        self.price_label.setObjectName("price_label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 121, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 91, 51))
        self.label_4.setObjectName("label_4")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(30, 90, 112, 131))
        self.splitter.setFrameShape(QtWidgets.QFrame.Panel)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.small_radio = QtWidgets.QRadioButton(self.splitter)
        self.small_radio.setObjectName("small_radio")
        self.medium_radio = QtWidgets.QRadioButton(self.splitter)
        self.medium_radio.setObjectName("medium_radio")
        self.large_radio = QtWidgets.QRadioButton(self.splitter)
        self.large_radio.setObjectName("large_radio")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(260, 90, 92, 131))
        self.splitter_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.cheese_option = QtWidgets.QCheckBox(self.splitter_2)
        self.cheese_option.setObjectName("cheese_option")
        self.olive_option = QtWidgets.QCheckBox(self.splitter_2)
        self.olive_option.setObjectName("olive_option")
        self.soda_option = QtWidgets.QCheckBox(self.splitter_2)
        self.soda_option.setObjectName("soda_option")
        self.water_option = QtWidgets.QCheckBox(self.splitter_2)
        self.water_option.setObjectName("water_option")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.calculate_button.setText(_translate("Dialog", "Calculate\n Price"))
        self.label.setText(_translate("Dialog", "Price"))
        self.price_label.setText(_translate("Dialog", "Please select ..."))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Select the Size</p><p align=\"center\">Of Pitza</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Select </p><p align=\"center\">Options</p></body></html>"))
        self.small_radio.setText(_translate("Dialog", "Small"))
        self.medium_radio.setText(_translate("Dialog", "Meduim"))
        self.large_radio.setText(_translate("Dialog", "Large"))
        self.cheese_option.setText(_translate("Dialog", "X Cheese"))
        self.olive_option.setText(_translate("Dialog", "X Olive"))
        self.soda_option.setText(_translate("Dialog", "Soda"))
        self.water_option.setText(_translate("Dialog", "Water"))
