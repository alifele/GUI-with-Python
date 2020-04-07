import sys
from PyQt5.QtWidgets import QApplication, QDialog
from main import *


class My_app(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.verticalSlider.setSingleStep(2)

    from _functions import update_status, update_status2



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
