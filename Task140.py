# Удалить определённый элемент из списка - все элементы.

a = [1, 2, 3, 3, 3, 1, 3, 2, 3, 3, 3]

while 3 in a:
    a.remove(3)

print(a)