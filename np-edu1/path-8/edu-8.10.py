from random import seed, randint


print("Перехват исключений.")
nums = [1, 2]
txt = "Python"
a = 10
names = [nums, a, txt]
seed(123)
for i in range(10):
    try:
        n = randint(0, 2)
        print("Сгенерировано число:", n)
        print("Количество элементов:", len(names[n]))
        names[n+1] //= n
    except TypeError as err:
        print("Ошибка:", err)
    except(LookupError, ArithmeticError) as err:
        print("Проблема с вычислениями:")
        print("Класс ошибки -", err.__class__)
    print("-" * 45)
print("Работа завершена.")
