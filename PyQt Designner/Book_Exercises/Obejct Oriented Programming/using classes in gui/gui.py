import sys
from PyQt5.QtWidgets import QApplication, QDialog
from main import *

class My_app(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.button_show.clicked.connect(self.update_show_label)
        self.ui.update_list.clicked.connect(self.update_listF)


    from _functions import update_show_label, update_listF



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
