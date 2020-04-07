def action_update(self, val):
    #text = self.ui.items.currentText()
    #self.ui.action_result.setText(text)
    self.ui.action_result.setText('{}'.format(val))

def Show_update(self):
    elem = self.ui.items.currentText()
    self.ui.buttom_result.setText(elem)
