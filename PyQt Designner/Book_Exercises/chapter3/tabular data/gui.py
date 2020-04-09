import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from main import *


class My_app(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.table.setItem(2,2,QTableWidgetItem('ali'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
