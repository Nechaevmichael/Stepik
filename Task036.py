# На вход поступают три целых числа - стороны треугольника.

# Необходимо вывести True, если данные стороны образуют прямоугольный треугольник, в противном случае - False.

# Для написания программы необходимо вспомнить теорему Пифагора

# Сделать задачу необходимо без использования условного оператора.

# Sample Input 1:

# 8 6 10
# Sample Output 1:

# True
a, b, c = map(int, input().split())
print(c == (a ** 2 + b ** 2)** (1/2) or b == (a ** 2 + c ** 2) ** (1/2) or a == (b ** 2 + c ** 2) ** (1/2))