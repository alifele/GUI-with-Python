import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import *


class My_app(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.show_button.clicked.connect(self.show_button_function)

    from functions import show_button_function



if __name__ == '__main__':

    App = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(App.exec_())
