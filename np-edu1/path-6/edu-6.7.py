# ПОЛЕ ОБЪЕКТА КЛАССА


class MyClass:
    name = "Класс MyClass"

    def set(self, n):
        self.nickname = n

    def get(self):
        print("Значение поля:", self.nickname)

    def __init__(self, n):
        self.set(n)
        print("Создан экземпляр класса.")
        self.get()

green = MyClass("Зелёный")
print("Принадлежность:", green.name)
red = MyClass("Красный")
print("Принадлежность:", red.name)
# MyClass.name = "Здесь могла быть ваша реклама!"
green.name = "Здесь был зелёный!"
red.name = "Здесь был красный!"
print("Спрашивает Красный:", red.name)
print("Спрашивает Зелёный:", green.name)
