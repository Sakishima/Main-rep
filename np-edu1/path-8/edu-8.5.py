# ИМПОРТ МАТЕМАТИЧЕСКИХ ФУЛНКЦИЙ (ДЕКОРАЦИИ ФУНКЦИЙ)


from math import exp, sin, cos, tan


def F(f):
    res = lambda x: exp(-f(x) ** 2)
    return res


def Q(f):
    def q(x):
        return tan(f(x))

    return q


@F
def f(x):
    return sin(x)


@F
def g(x):
    return cos(x)


@Q
@F
def h(x):
    return x


n = 5
print("Функция f():")
for i in range(n + 1):
    z = i / n
    print(f(z), "->", exp(-sin(z) ** 2))
print("Функция g():")
for i in range(n + 1):
    z = i / n
    print(g(z), "->", exp(-cos(z) ** 2))
print("Функция h():")
for i in range(n + 1):
    z = i / n
    print(h(z), "->", tan(exp(-z ** 2)))
