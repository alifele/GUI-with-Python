def update_status(self, value):
    self.ui.lineEdit.setText('{}'.format(value))

def update_status2(self, value, value2):
    self.ui.lineEdit.setText('{}, {}'.format(value, value2))
