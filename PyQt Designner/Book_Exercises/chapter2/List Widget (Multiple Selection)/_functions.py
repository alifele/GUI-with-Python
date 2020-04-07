def update_list(self):

    self.ui.selected.clear()
    items = self.ui.List.selectedItems()

    for i in items:
        self.ui.selected.addItem(i.text())
