from PyQt5.QtWidgets import QInputDialog, QListWidgetItem



def add_to_list(self):
    value = self.ui.input_name.text()
    self.ui.List.addItem(value)
    self.ui.input_name.clear()
    #self.ui.List.setFocus()



def del_list(self):
    item = self.ui.List.currentRow()
    self.ui.List.takeItem(item)


def edit_list(self):
    row = self.ui.List.currentRow()
    newtext, ok = QInputDialog.getText(self, "Enter New Text",
    'Please Enter the New Value')

    if ok and (len(newtext) != 0):
        self.ui.List.takeItem(self.ui.List.currentRow())
        self.ui.List.insertItem(row, newtext)
        #self.ui.List.insertItem(row, QListWidgetItem(newtext))
        #You can do both ways to add new items to the list

def delete_all(self):
    self.ui.List.clear()
