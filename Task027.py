# На вход поступает целое число.

# Программа должна вывести True, если введенное значение кратно 6 (без остатка делится на 6), в противном случае - False

# Сделать задачу необходимо без использования условного оператора.

# Sample Input 1:

# 30
# Sample Output 1:

# True
number = int(input())
print(number % 6 == 0)