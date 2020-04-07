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
        Dialog.resize(745, 249)
        self.calculate = QtWidgets.QPushButton(Dialog)
        self.calculate.setGeometry(QtCore.QRect(230, 180, 261, 25))
        self.calculate.setObjectName("calculate")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 30, 661, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.amout_book = QtWidgets.QSpinBox(self.widget)
        self.amout_book.setObjectName("amout_book")
        self.gridLayout.addWidget(self.amout_book, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.price_sugar = QtWidgets.QLineEdit(self.widget)
        self.price_sugar.setObjectName("price_sugar")
        self.gridLayout.addWidget(self.price_sugar, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 4, 1, 1)
        self.price_book = QtWidgets.QLineEdit(self.widget)
        self.price_book.setObjectName("price_book")
        self.gridLayout.addWidget(self.price_book, 0, 2, 1, 1)
        self.total_sugar = QtWidgets.QLineEdit(self.widget)
        self.total_sugar.setReadOnly(True)
        self.total_sugar.setObjectName("total_sugar")
        self.gridLayout.addWidget(self.total_sugar, 1, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)
        self.total_book = QtWidgets.QLineEdit(self.widget)
        self.total_book.setReadOnly(True)
        self.total_book.setObjectName("total_book")
        self.gridLayout.addWidget(self.total_book, 0, 6, 1, 1)

        self.retranslateUi(Dialog)
        self.calculate.clicked['bool'].connect(Dialog.update_book_price)
        self.calculate.clicked['bool'].connect(Dialog.update_sugar_price)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.calculate.setText(_translate("Dialog", "Calculate"))
        self.label_4.setText(_translate("Dialog", "total price"))
        self.label.setText(_translate("Dialog", "Book Price"))
        self.label_2.setText(_translate("Dialog", "Sugar Price"))
        self.label_3.setText(_translate("Dialog", "total price"))
