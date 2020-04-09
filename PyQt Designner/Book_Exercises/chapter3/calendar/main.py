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
        Dialog.resize(515, 411)

        self.Date = QtCore.QDate()

        self.calendar = QtWidgets.QCalendarWidget(Dialog)
        self.calendar.setGeometry(QtCore.QRect(10, 10, 481, 171))
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Saturday)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName("calendar")
        self.show = QtWidgets.QPushButton(Dialog)
        self.show.setGeometry(QtCore.QRect(40, 250, 131, 71))
        self.show.setObjectName("show")
        self.date = QtWidgets.QDateEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(320, 270, 110, 26))
        self.date.setObjectName("date")
        self.date.setDisplayFormat('yyyy/MM/dd')

        self.retranslateUi(Dialog)
        self.show.clicked.connect(Dialog.update_calendar)
        self.calendar.selectionChanged.connect(Dialog.update_date)
        self.date.dateChanged['QDate'].connect(Dialog.update_bigCalendar)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.show.setText(_translate("Dialog", "Show Today"))
