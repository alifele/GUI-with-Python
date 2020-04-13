from PyQt5.QtWidgets import QInputDialog

def open_name_dialog_F(self):
    name, status = QInputDialog.getText(self, 'enter your name', 'please enter your name')

    if status == True:
        self.ui.name_enter.setText(name)


def open_age_dialog_F(self):
    age, status = QInputDialog.getInt(self, 'enter your age', 'please enter your age',
    18, 15, 59, 1)

    if status == True:
        self.ui.age_enter.setText(str(age))

def open_weight_dialog_F(self):

    weight, status = QInputDialog.getDouble(self, 'enter your weight', 'please enter your weight',
    60, 55, 95, 3)

    if status == True:
        self.ui.weight_enter.setText(str(weight))


def open_country_dialog_F(self):

    country, status = QInputDialog.getItem(self, 'enter your name', 'please enter your name',
    self.country_list, 0, False)

    if status == True:
        self.ui.country_enetr.setText(country)
