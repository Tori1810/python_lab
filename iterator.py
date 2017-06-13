

class Iterator:
    """ Class Iterator for database"""

    def __init__(self, base):
        self.base = base
        self.start = 0
        self.stop = len(base)
        self.index = self.start - 1

    def __next__(self):
        self.index += 1
        if self.index == self.stop:
            raise StopIteration
