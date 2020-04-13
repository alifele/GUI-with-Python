from PyQt5.QtWidgets import QFontDialog

def open_font_dialog(self):
    font, status = QFontDialog.getFont()

    if status == True:

        self.ui.TEXT.setFont(font)
