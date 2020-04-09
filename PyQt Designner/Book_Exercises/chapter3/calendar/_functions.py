def update_date(self):
    data = self.ui.calendar.selectedDate()
    self.ui.date.setDate(data)

def update_calendar(self):
    today = self.ui.Date.currentDate()
    self.ui.date.setDate(today)
    self.ui.calendar.setSelectedDate(today)



def update_bigCalendar(self, val):
    self.ui.calendar.setSelectedDate(val)
