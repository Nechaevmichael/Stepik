# На вход поступают два целых числа.

# Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.

# Сделать задачу необходимо без использования условного оператора.

# Sample Input 1:

# 77 14
# Sample Output 1:

# True
a, b = map(int, input().split())
print(a % 7 == 0 and b % 7 == 0)