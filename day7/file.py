class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __sizeof__(self):
        return self.size

    def __repr__(self):
        return self.name + ': ' + self.size