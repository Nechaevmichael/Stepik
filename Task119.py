# На вход вашей программе поступает два неравных друг друг целых числа в отдельных строках
# Ваша задача сохранить наименьшее из этих чисел в переменную  minimum, а наибольшее - в maximum
# Использовать нужно, конечно же, тернарный оператор
# В качестве ответа выведите через пробел сперва minimum , а потом maximum
# Sample Input 1:
# 8
# 11
# Sample Output 1:
# 8 11

a = int(input())
b = int(input())
# if a < b:
#     minimum = a
#     maximum = b
#     print(minimum, maximum)
# else:
#     minimum = b
#     maximum = a
minimum = a if a < b else b
maximum = b if a < b else a
print(minimum, maximum)