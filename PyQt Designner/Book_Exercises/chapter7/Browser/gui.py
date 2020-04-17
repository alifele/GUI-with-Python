import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from main import *

class My_app(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui,setupUi(self)

        self.ui.pushButton.clicked.connect(self.dispsite)


    def dispsite(self):
        self.ui.widget.load(QUrl(self.ui.lineEdit.text()))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = My_app()
    window.show()
    sys.exit(app.exec_())
