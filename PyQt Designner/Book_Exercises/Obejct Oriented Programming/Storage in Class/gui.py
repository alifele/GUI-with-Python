import sys
from PyQt5.QtWidgets import QApplication, QDialog
from main import *
from _classes import *

class My_app(QDialog):

    def __init__(self):

        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self, MName)

        self.uii = MName()
        self.uii.setup()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
