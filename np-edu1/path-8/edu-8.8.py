# ФУНКЦИЯ С АННОТАЦИЯМИ


def show(a: "первый аргумент", b: int = 0) -> None:
    print("a =", a)
    print("b =", b)


show(10)
show(10, 20)
print(show.__annotations__)
annt = show.__annotations__["a"]
print("Аргумент a:", annt)
res = show.__annotations__["return"]
print("Возвращаемый результат:", res)
