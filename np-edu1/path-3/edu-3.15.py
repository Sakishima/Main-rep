# ВЫЧИСЛЕНИЕ ФАКТОРИАЛА И ДВОЙНОГО ФАКТОРИАЛА


def factor(mode=True):
    # функция для вычислений простого факториала
    def sf(n):
        s = 1  # Начальное значение произведения
        i = n  # Начальное значение индекса
        while i > 1:
            s *= i
            i -= 1
        return s

    # функция для вычисления двойного факториала
    def df(n):
        s = 1  # Начальное значение произведения
        i = n  # Начальное значение индекса
        while i > 1:
            s *= i
            i -= 2
        return s

    if mode:
        return sf
    else:
        return df


print("5! =", factor()(5))
print("5! =", factor(True)(5))
print("5!! =", factor(False)(5))
