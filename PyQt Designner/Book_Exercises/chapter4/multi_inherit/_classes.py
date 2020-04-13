class StudentCls():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


class MarkCls():
    def __init__(self, Hmark, Gmark):
        self.Hmark = Hmark
        self.Gmark = Gmark

    def get_Hmark(self):
        return self.Hmark

    def get_Gmark(self):
        return self.Gmark



class ResultCls(MarkCls, StudentCls):

    def __init__(self, name, code, Hmark, Gmark):

        MarkCls.__init__(self, Hmark, Gmark)
        StudentCls.__init__(self, name, code)
