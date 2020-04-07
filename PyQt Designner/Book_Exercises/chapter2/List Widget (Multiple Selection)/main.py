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
        Dialog.resize(456, 357)
        self.List = QtWidgets.QListWidget(Dialog)
        self.List.setGeometry(QtCore.QRect(20, 20, 251, 81))
        self.List.setObjectName("List")
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.List.addItem(item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 220, 171, 21))
        self.label.setObjectName("label")
        self.selected = QtWidgets.QListView(Dialog)
        self.selected.setGeometry(QtCore.QRect(170, 160, 256, 192))
        self.selected.setObjectName("selected")

        self.retranslateUi(Dialog)
        self.List.itemSelectionChanged.connect(Dialog.update_list)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.List.isSortingEnabled()
        self.List.setSortingEnabled(False)
        item = self.List.item(0)
        item.setText(_translate("Dialog", "Phys"))
        item = self.List.item(1)
        item.setText(_translate("Dialog", "Math"))
        item = self.List.item(2)
        item.setText(_translate("Dialog", "Chem"))
        item = self.List.item(3)
        item.setText(_translate("Dialog", "Elec"))
        item = self.List.item(4)
        item.setText(_translate("Dialog", "Surface"))
        item = self.List.item(5)
        item.setText(_translate("Dialog", "Nano"))
        item = self.List.item(6)
        item.setText(_translate("Dialog", "Optics"))
        self.List.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "You Have Selected:"))
