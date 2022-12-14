# Вашей программе будут поступать на вход N списков, содержащих целые числа

# Для каждого введенного списка определите, сколько в нем встречается различных чисел.

# Входные данные

# Сперва поступает натуральное число N - количество списков

# В следующих N строк вводятся значения каждого списка, разделенные через пробел

# Выходные данные

# Вывести на отдельной строке количество различных чисел каждого введенного списка в том же порядке, в котором вводились списки

N = int(input())

for i in range(N):
    print(len(set(map(int, input().split()))))