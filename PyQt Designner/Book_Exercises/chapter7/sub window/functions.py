


def cascade_function(self):
    self.ui.mdiArea.setViewMode(0)
    self.ui.mdiArea.cascadeSubWindows()



def tabbed_function(self):
    self.ui.mdiArea.setViewMode(1)
    self.ui.mdiArea.setTabsClosable(True)
    self.ui.mdiArea.setTabsMovable(True)
    #self.ui.mdiArea.tabs



def sub_function(self):
    self.ui.mdiArea.setViewMode(0)




def tile_function(self):
    self.ui.mdiArea.setViewMode(0)
    self.ui.mdiArea.tileSubWindows()



def update_info(self):
    name = self.ui.name_lineEdit.text()
    age = self.ui.age_lineEdit.text()
    family = self.ui.family_lineEdit.text()


    self.ui.info_label.setText(name + age + family)
