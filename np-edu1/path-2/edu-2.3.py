# Пользователь вводит значение
res = eval(input("Введите что-нибудь: "))
# Тип значения запоминаем в переменной
resType = type(res)
# Используем условные операторы (упрощённая форма) для проверки типа введённого пользователем значения
if resType == int:
    # Если целое число
    print("Это целое число!")
elif resType == float:
    # Если действительное число
    print("Это действительное число!")
else:
    # Если не число
    print("Наверное, это текст!")
# После выполнения условных операторов
print("Работа завершена!")