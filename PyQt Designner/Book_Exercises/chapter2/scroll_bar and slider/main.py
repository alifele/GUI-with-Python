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
        Dialog.resize(571, 520)
        Dialog.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 91, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 240, 81, 17))
        self.label_4.setObjectName("label_4")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(100, 280, 16, 160))
        self.verticalScrollBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(270, 270, 16, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(400, 360, 113, 25))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(400, 330, 67, 17))
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 40, 105, 88))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(150, 40, 241, 91))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.widget1)
        self.horizontalScrollBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout_2.addWidget(self.horizontalScrollBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalSlider = QtWidgets.QSlider(self.widget1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)

        self.retranslateUi(Dialog)
        self.horizontalSlider.sliderMoved['int'].connect(Dialog.update_status)
        self.horizontalScrollBar.actionTriggered['int'].connect(Dialog.update_status)
        self.verticalScrollBar.rangeChanged['int', 'int'].connect(Dialog.update_status2)
        self.verticalSlider.valueChanged['int'].connect(Dialog.update_status)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Pulse Rate"))
        self.label_4.setText(_translate("Dialog", "Cholestrol"))
        self.label_5.setText(_translate("Dialog", "Status"))
        self.label.setText(_translate("Dialog", "blood pressure"))
        self.label_2.setText(_translate("Dialog", "blood sugar"))
