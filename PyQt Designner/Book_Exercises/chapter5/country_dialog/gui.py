import sys
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog
from main import *


class My_app(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.country_list = ['Iran', 'Us', 'Switzerland', 'Canada']

    from _functions import open_age_dialog_F, open_name_dialog_F
    from _functions import open_country_dialog_F, open_weight_dialog_F




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
