from _classes import *

def update_show_label(self):
    name = self.ui.name_enter.text()
    self.ui.name_enter.clear()
    labelname = LabelName(name)
    self.ui.lable_show.setText(labelname.return_name(-1))



def update_listF(self):
    self.ui.names_list.clear()
    for i in range(len(LabelName.Names)):
        self.ui.names_list.addItem(LabelName.Names[i])
