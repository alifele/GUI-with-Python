def update_book_price(self):
    book_p = int(self.ui.price_book.text())
    book_n = int(self.ui.amout_book.text())

    self.ui.total_book.setText('{}'.format(book_n*book_p))

def update_sugar_price(self):
    sugar_p = int(self.ui.price_sugar.text())
    sugar_n = float(self.ui.doubleSpinBox.text())

    self.ui.total_sugar.setText('{}'.format(sugar_p*sugar_n))
