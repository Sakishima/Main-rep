print("Решаем уравнение ax=b")
try:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    x = b/a
    print("Решение уравнения: x =", x)
except ValueError:
    print("Нужно было ввести число.")
except ZeroDivisionError:
    print("Внимание! На ноль делить нельзя!")
print("Работа программы завершена.")
