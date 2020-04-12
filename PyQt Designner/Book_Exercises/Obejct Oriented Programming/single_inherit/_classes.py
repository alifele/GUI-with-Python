class Studentcls():
    def __init__(self, code, name):

        self.code = code
        self.name = name

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


class Markcls(Studentcls):

    def __init__(self, code, name, Gmark, Hmark):
        super().__init__(code, name)

        self.Gmark = Gmark
        self.Hmark = Hmark

    def get_Gmark(self):
        return self.Gmark

    def get_Hmark(self):
        return self.Hmark
