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
        Dialog.resize(480, 300)
        self.List = QtWidgets.QListWidget(Dialog)
        self.List.setGeometry(QtCore.QRect(20, 20, 181, 101))
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
        self.result = QtWidgets.QLineEdit(Dialog)
        self.result.setGeometry(QtCore.QRect(160, 160, 231, 25))
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 160, 131, 17))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        #self.List.itemClicked['QListWidgetItem*'].connect(Dialog.update_result)
        #self.List.itemDoubleClicked['QListWidgetItem*'].connect(Dialog.update_result)
        #self.List.clicked.connect(Dialog.update_result)
        self.List.itemSelectionChanged.connect(Dialog.update_result)

        #self.List.itemChanged['QListWidgetItem*'].connect(Dialog.update_result)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.List.isSortingEnabled()
        self.List.setSortingEnabled(False)
        item = self.List.item(0)
        item.setText(_translate("Dialog", "Mathematics"))
        item = self.List.item(1)
        item.setText(_translate("Dialog", "Physics"))
        item = self.List.item(2)
        item.setText(_translate("Dialog", "Chemistry"))
        item = self.List.item(3)
        item.setText(_translate("Dialog", "Neuroscience"))
        item = self.List.item(4)
        item.setText(_translate("Dialog", "Electical Eng."))
        item = self.List.item(5)
        item.setText(_translate("Dialog", "Surface Technology"))
        item = self.List.item(6)
        item.setText(_translate("Dialog", "LED based test"))
        self.List.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "You have selected"))
