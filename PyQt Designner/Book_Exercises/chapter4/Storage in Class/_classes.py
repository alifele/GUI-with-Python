from gui import My_app
from main import *

class MName():

    def setup(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(My_app, self)


    def show_name():
        self.name = self.ui.lineEdit.text()
        self.ui.label.setText(self.name)
