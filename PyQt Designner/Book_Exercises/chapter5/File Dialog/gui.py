import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction
from main import *


class My_app(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    from _functions import save_file, open_file


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
