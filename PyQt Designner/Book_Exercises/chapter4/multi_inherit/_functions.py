
from _classes import *


def compute_button(self):

    name = self.ui.name_enter.text()
    code = self.ui.code_enter.text()
    Hmark = self.ui.his_enter.text()
    Gmark = self.ui.geo_enter.text()


    resultobj = ResultCls(name, code, Hmark, Gmark)


    sum = int(resultobj.get_Gmark()) + int(resultobj.get_Hmark())
    self.ui.total_show.setText(str(sum))
    self.ui.average_show.setText(str(sum/2))
