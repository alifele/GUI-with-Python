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
        Dialog.resize(469, 467)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setGeometry(QtCore.QRect(60, 90, 241, 191))
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 0, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "0"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "1"))
        item = self.table.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "2"))
        item = self.table.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        item = self.table.item(0, 0)
        item.setText(_translate("Dialog", "ali"))
        self.table.setSortingEnabled(__sortingEnabled)
