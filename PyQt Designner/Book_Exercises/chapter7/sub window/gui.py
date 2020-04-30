import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Main import *



class My_app(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.ui.family_subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.name_subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.extra_info_subwindow)
        self.ui.mdiArea.tileSubWindows()





    from functions import cascade_function, tabbed_function, sub_function, tile_function
    from functions import update_info





if __name__ == "__main__":

    App  = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(App.exec_())
