import sys
from PyQt5.QtWidgets import QApplication, QDialog
from main import *

class My_app(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        self.ui.timer.start(1000)
        self.ui.timer.timeout.connect(self.update_lcd)

    from _functions import update_lcd

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = My_app()
    while 1 :
        window.ui.timer.start(1000)
        window.show()
    sys.exit(app.exec_())


















if __name__ == "__main":
    app = QApplication()
    window = My_app()
    window.show()
    sys.exit(app.exec_())
