# ВЫЧИСЛЕНИЕ ФАКТОРИАЛА И ДВОЙНОГО ФАКТОРИАЛА (#2)


def factor(mode=True):
    # функция для вычислений простого факториала
    def f(n, d):
        s = 1  # Начальное значение произведения
        i = n  # Начальное значение индекса
        while i > 1:
            s *= i
            i -= d
        return s
    d = 1 if mode else 2
    return lambda n: f(n, d)


print("5! =", factor()(5))
print("5! =", factor(True)(5))
print("5!! =", factor(False)(5))
