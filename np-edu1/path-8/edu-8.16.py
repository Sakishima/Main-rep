# ИТЕРАТОР ДЛЯ ЧИСЕЛ ФИБОНАЧЧИ


class Fibs:
    def __init__(self, n):
        self.start()
        self.n = n

    def start(self):
        self.count = 1
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            self.start()
            raise StopIteration
        res = self.a
        self.a, self.b = self.b, self.a+self.b
        self.count += 1
        return res


obj = Fibs(10)
for s in obj:
