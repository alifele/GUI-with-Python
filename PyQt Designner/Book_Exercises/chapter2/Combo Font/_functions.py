from myimports import *


'''
def UpdateText(self):
    #myFont = QtGui.QFont(self.ui.font_list.itemText(self.ui.font_list.currentIndex()), 15)
    myFont = QtGui.QFont(self.ui.font_list.currentItem().text(), 15)

    self.ui.textBrowser.setFont(myFont)
'''

def UpdateText(self, val):
    #myFont = QtGui.QFont(self.ui.font_list.itemText(self.ui.font_list.currentIndex()), 15)
    myFont = QtGui.QFont(val, 15)

    self.ui.textBrowser.setFont(myFont)
