import sys
from PyQt5.QtWidgets import QApplication, QDialog
from layout import *

class My_app(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.var = 0

        self.ui.meduim.toggled.connect(self.val_update)
        self.ui.small.toggled.connect(self.val_update)
        self.ui.xlarge.toggled.connect(self.val_update)
        self.ui.large.toggled.connect(self.val_update)

        self.ui.cal.clicked.connect(self.cal_show)
        self.show()


    def cal_show(self):
        self.ui.price_label.setText('{}'.format(self.var))

    def val_update(self):
        if self.ui.meduim.isChecked() == True:
            self.var = 10

        if self.ui.small.isChecked() == True:
            self.var = 20

        if self.ui.xlarge.isChecked() == True:
            self.var = 30

        if self.ui.large.isChecked() == True:
            self.var = 40



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
