class StudentCls():
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


class MarkCls(StudentCls):
    def __init__(self, code, name, Hmark, Gmark):
        super().__init__(code, name)
        self.Hmark = Hmark
        self.Gmark = Gmark

    def get_Hmark(self):
        return self.Hmark

    def get_Gmark(self):
        return self.Gmark


class ResultCls(MarkCls):
    def __init__(self,code, name, Hmark, Gmark):
        super().__init__(code, name, Hmark, Gmark)
