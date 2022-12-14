# Перед вами располагается два множества  set_a и set_b

# Ваша задача вывести на экран количество элементов, которое содержится в результате пересечения множеств set_a и set_b

set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
         76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}

set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
         33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}

print(len(set_a & set_b))
print(len(set_a.intersection(set_b)))