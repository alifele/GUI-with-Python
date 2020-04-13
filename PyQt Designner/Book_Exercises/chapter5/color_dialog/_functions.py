from PyQt5.QtWidgets import QColorDialog

def show_color_dialog_F(self):

    self.color = QColorDialog.getColor()

    if self.color.isValid():

        #self.ui.color_frame.setStyleSheet("QWidget { background-color: %s }" % self.color.name())
        self.ui.color_frame.setStyleSheet("QWidget { background-color: %s }" % self.color.name())
        self.ui.color_label.setText(str(self.color.name()))
