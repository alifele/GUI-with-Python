def add(self):
    a = int(self.ui.input1.text())
    b = int(self.ui.input2.text())

    self.result = a+b


def mult(self):
    a = int(self.ui.input1.text())
    b = int(self.ui.input2.text())

    self.result = a*b


def dev(self):
    a = int(self.ui.input1.text())
    b = int(self.ui.input2.text())

    self.result = a/b


def sub(self):
    a = int(self.ui.input1.text())
    b = int(self.ui.input2.text())

    self.result = a-b

def show_cal(self):
    self.ui.result.setText('{}'.format(self.result))
