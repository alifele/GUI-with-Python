import sys
from PyQt5.QtWidgets import QDialog, QApplication
from welcome import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        self.ui.label.setText('Hello ' + self.ui.lineEditName.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())
