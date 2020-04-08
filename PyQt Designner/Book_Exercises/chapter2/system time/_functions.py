from PyQt5 import QtCore

def update_lcd(self):
    time = QtCore.QTime.currentTime()
    text = time.toString('hh:mm')
    self.ui.Time.display(text)
