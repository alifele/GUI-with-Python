from main import *
from gui import *

class MName():

    def __init__(self):

        self.ui = Ui_Dialog()
        self.ui.setupUi(My_app, self)

    def show_dialog(self):
        self.val = self.ui.name.val()
        print('hello')
