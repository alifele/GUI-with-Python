import sys
from PyQt5.QtWidgets import QApplication, QDialog
from layout import *


class My_app(QDialog):

    def __init__(self):

        super().__init__()
        self.val = 10
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def update_val(self):
        self.val += 10

    def incval(self):
        self.val += 20

    def showcal(self):
        self.ui.price_label.setText('{}'.format(self.val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
