def show_button_function(self):

    Email = self.ui.email_lineEdit.text()
    Pass = self.ui.pass_lineEdit.text()
    self.ui.email_pass_label.setText(Email +'\n' +  Pass)
