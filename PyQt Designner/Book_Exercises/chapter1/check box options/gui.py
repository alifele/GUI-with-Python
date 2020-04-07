import sys
from PyQt5.QtWidgets import QApplication, QDialog
from layout import *


class My_app(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.val = 0

        self.ui.small_radio.toggled.connect(self.update_val)
        self.ui.medium_radio.toggled.connect(self.update_val)
        self.ui.large_radio.toggled.connect(self.update_val)

        self.ui.calculate_button.clicked.connect(self.cal_show)

        self.ui.cheese_option.stateChanged.connect(self.update_opt)
        self.ui.olive_option.stateChanged.connect(self.update_opt)
        self.ui.soda_option.stateChanged.connect(self.update_opt)
        self.ui.water_option.stateChanged.connect(self.update_opt)


    def update_opt(self):

        if self.ui.cheese_option.isChecked() == True:
            self.val += 10
        if self.ui.olive_option.isChecked() == True:
            self.val += 10
        if self.ui.soda_option.isChecked() == True:
            self.val += 10
        if self.ui.water_option.isChecked() == True:
            self.val += 10

    def cal_show(self):
        self.ui.price_label.setText('The price is: {}'.format(self.val))



    def update_val(self):


        if self.ui.small_radio.isChecked() == True:
            self.val += 10

        if self.ui.small_radio.isChecked() == True:
            self.val += 20

        if self.ui.small_radio.isChecked() == True:
            self.val += 30


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
