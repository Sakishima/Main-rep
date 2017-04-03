# Функция без аргументов
def your_name():
    print("Добрый день!")
    name = input("Как вас зовут? ")
    return name


# Функция с одним аргументом
def say_hello(txt):
    print("Здравствуйте,", txt + "!")


my_name = your_name()
say_hello(my_name)
