def update_show(self):

    N = self.ui.nDays.value()
    Type = self.ui.roomType.currentText()
    Day = str(self.ui.calendar.selectedDate().toPyDate())


    self.ui.resultShow.setText('number of days: {}\n'.format(N) + 'Room Type: ' + Type +
    "\nDate: " +  Day + '\n' + 'price: 14$')
