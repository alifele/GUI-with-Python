from _classes import *


def update_text(self):
    name = self.ui.name_enter.text()
    code = self.ui.code_enter.text()
    Gmark = self.ui.Geo_enter.text()
    Hmark = self.ui.history_enter.text()

    studentobj = Studentcls(name, code)
    markobj = Markcls(name, code, Gmark, Hmark)


    self.ui.TEXTs.setText(markobj.get_Gmark() + '\n' + markobj.get_Hmark() + '\n'
                          + studentobj.get_name() + '\n' + studentobj.get_code())
