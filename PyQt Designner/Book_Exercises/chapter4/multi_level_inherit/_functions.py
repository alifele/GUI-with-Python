from _classes import *

def compute_button(self):

    code = self.ui.code_enter.text()
    name = self.ui.name_enter.text()
    Hmark = self.ui.his_enter.text()
    Gmark = self.ui.geo_enter.text()

    ResultObj = ResultCls(code, name, Hmark, Gmark)

    sum = int(ResultObj.get_Gmark()) + int(ResultObj.get_Hmark())
    
    self.ui.total_show.setText(str(sum))
    self.ui.average_show.setText(str(sum/2))
