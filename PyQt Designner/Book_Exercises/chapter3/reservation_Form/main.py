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
        Dialog.resize(539, 482)
        self.calendar = QtWidgets.QCalendarWidget(Dialog)
        self.calendar.setGeometry(QtCore.QRect(40, 30, 456, 171))
        self.calendar.setObjectName("calendar")
        self.nDays = QtWidgets.QSpinBox(Dialog)
        self.nDays.setGeometry(QtCore.QRect(50, 260, 111, 26))
        self.nDays.setObjectName("nDays")
        self.calculate = QtWidgets.QPushButton(Dialog)
        self.calculate.setGeometry(QtCore.QRect(150, 320, 89, 25))
        self.calculate.setObjectName("calculate")
        self.resultShow = QtWidgets.QLabel(Dialog)
        self.resultShow.setGeometry(QtCore.QRect(150, 370, 261, 101))
        self.resultShow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultShow.setTextFormat(QtCore.Qt.AutoText)
        self.resultShow.setWordWrap(False)
        self.resultShow.setObjectName("resultShow")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 151, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 230, 151, 17))
        self.label_3.setObjectName("label_3")
        self.roomType = QtWidgets.QComboBox(Dialog)
        self.roomType.setGeometry(QtCore.QRect(280, 260, 181, 25))
        self.roomType.setObjectName("roomType")
        self.roomType.addItem("")
        self.roomType.addItem("")
        self.roomType.addItem("")
        self.roomType.addItem("")
        self.roomType.addItem("")

        self.retranslateUi(Dialog)
        self.calculate.clicked.connect(Dialog.update_show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.calendar, self.nDays)
        Dialog.setTabOrder(self.nDays, self.roomType)
        Dialog.setTabOrder(self.roomType, self.calculate)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.calculate.setText(_translate("Dialog", "&calculate"))
        self.resultShow.setText(_translate("Dialog", "<html><head/><body><p>Please </p><p>Select ...</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Select number of days"))
        self.label_3.setText(_translate("Dialog", "Select Room Type"))
        self.roomType.setItemText(0, _translate("Dialog", "single rom"))
        self.roomType.setItemText(1, _translate("Dialog", "shared room"))
        self.roomType.setItemText(2, _translate("Dialog", "shared room + hand wash"))
        self.roomType.setItemText(3, _translate("Dialog", "single room + hand wash"))
        self.roomType.setItemText(4, _translate("Dialog", "shared room + bathroom"))
