# ПОЛЕ ЭКЗЕМПЛЯРА КЛАССА


class MyClass:
    def set(self, n):
        print("Внимание! Присваивается значение!")
        self.number = n

    def get(self):
        print("Значение поля:", self.number)

    def __init__(self, n=0):
        self.set(n)

    def __del__(self):
        print("Всем пока!")

obj = MyClass()
obj.set(100)
obj.get()
del obj
