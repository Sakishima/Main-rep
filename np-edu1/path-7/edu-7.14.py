class MyClass:
    def __setattr__(self, key, value):
        print("Выполняется метод __setattr__():")
        txt = "*\tПолю " + str(key)
        txt += " присваивается значение " + str(value)
        print(txt)
        self.__dict__[key] = value
        print("Метод __setattr__() выполнен.")

    def __getattribute__(self, item):
        print("Выполняется метод __getattribute__():")
        txt = "*\tСчитывается значение поля " + str(item)
        print(txt)
        try:
            res = object.__getattribute__(self, item)
        except AttributeError:
            res = "У экземпляра поля " + str(item) + " нет!"
        print("Метод __getattribute__() завершает работу.")
        return res

    def __delattr__(self, item):
        print("Выполняется метод __delattr__():")
        txt = "*\tУдаляется поле " + str(item)
        print(txt)
        try:
            del self.__dict__[item]
        except KeyError:
            print("Нельзя удалить поле " + str(item))
        print("Метод __delattr__() выполнен.")


obj = MyClass()
obj.name = "Pyton"
print("Значение поля name:", obj.name)
del obj.name
print(obj.name)
del obj.name
