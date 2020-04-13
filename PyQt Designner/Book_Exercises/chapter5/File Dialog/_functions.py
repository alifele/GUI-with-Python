from PyQt5.QtWidgets import QFileDialog

def open_file(self):

    fname = QFileDialog.getOpenFileName(self, 'Choose your file', '/home',
    'Images (*.png, *.jph);; Text files (*.txt);;XML files (.xml)')
    if fname[0]:
        f = open(fname[0], 'r')
        print(fname)

        with f :
            data = f.read()
            self.ui.textEdit.setText(data)


def save_file(self):
    options = QFileDialog.Options()
    fname, _ = QFileDialog.getSaveFileName(self, 'Where to save ?',
    'Images (*.png, *.jph);; Text files (*.txt);;XML files (.xml)',options= options )

    f = open(fname, 'w')
    text = self.ui.textEdit.toPlainText()
    f.write(text)
    f.close()
