

class LabelName():
    Names = []
    def __init__(self, name):
        self.name = name
        LabelName.Names.append(name)

    def return_name(self, i=-1):
        return LabelName.Names[i]
