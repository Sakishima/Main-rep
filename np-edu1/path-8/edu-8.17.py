# ФУНКЦИЯ-ГЕНЕРАТОР ДЛЯ ЧИСЕЛ ФИБОНАЧЧИ


def fibs_gen(n):
    a = 1
    b = 1
    for i in range(n):
        res = a
        a, b = b, a+b
        yield res


print("Попытка №1")
for s in fibs_gen(10):
    print(s, end=" ")
print("\nПопытка №2")
for s in fibs_gen(10):
    print(s, end=" ")
print("\nПопытка №3")
f = fibs_gen(15)
for s in f:
    print(s, end=" ")
print("\nПопытка №4")
for s in f:
    print(s, end=" ")
print("Завершение работы.")
