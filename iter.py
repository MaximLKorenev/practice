class List2:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.start = self.start
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count < 10:
            return current
        raise StopIteration


class List3:
    def __init__(self, n, loop):
        self.n = n
        self.loop = loop

    def __iter__(self):
        self.start = 1
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count < self.n:
            return current
        if self.loop:
            self.start = 1
            self.count = 0
            return self.__next__()
        else:
            raise StopIteration
