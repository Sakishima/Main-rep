class Adder:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        txt = "Значение поля number = "
        txt += str(self.number)
        return txt

    def __add__(self, x):
        number = self.number + x
        tmp = Adder(number)
        return tmp


a = Adder(10)
b = a + 5
print(a)
print(b)
