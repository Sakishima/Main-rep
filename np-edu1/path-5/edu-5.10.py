# РАБОТА СО СЛОВАРЯМИ

symbs = dict([["a", "первый"], ["b", "второй"]])
more_symbs = dict([["c", "третий"], ["d", "четвёртый"]])
symbs.update(more_symbs)
print("Словарь:", symbs)
print("Количество ключей в словаре:", len(symbs))
print("Элемент с ключём 'с':", symbs.get("c", "Нет такого ключа!"))
print("Наличие элемента с ключём 'с':", "c" in symbs)
del symbs["c"]
print("Словарь:", symbs)
print("Элемент с ключом 'c':", "c" in symbs)
print("Ключи словаря:", list(symbs.keys()))
print("Значения элементов словаря:", list(symbs.values()))
print("Содержимое словаря:", list(symbs.items()))
print("Удаляется элемент со значением:", symbs.pop("b"))
print("Словарь:", symbs)
symbs.clear()
print("Словарь:", symbs)
