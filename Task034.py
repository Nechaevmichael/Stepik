
# На вход поступают три целых числа - стороны треугольника.

# Необходимо вывести True, если данные стороны образуют равнобедренный треугольник, в противном случае - False.

# Сделать задачу необходимо без использования условного оператора.

# Sample Input 1:

# 4 6 9
# Sample Output 1:

# False
# Sample Input 2:

# 7 8 7
# Sample Output 2:

# True
a, b, c = map(int, input().split())
print(a == b or a == c)