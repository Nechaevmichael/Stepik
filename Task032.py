# На вход поступает целое число.

# Программа должна вывести True, если введенное значение принадлежит интервалу от 5 не включительно до 19 включительно ,
#  в противном случае - False.

# Сделать задачу необходимо без использования условного оператора.

# Sample Input 1:

# 10
# Sample Output 1:

# True

number = int(input())
print(number > 5 and number <= 19)