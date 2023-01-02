# Напишите функцию check_sum, которая принимает произвольное количество аргументов типа int.

# Данная функция должна выводить not enough, если сумма всех элементов меньше 50, в противном случае выводить verification passed

# Вам необходимо написать только определение функции check_sum

# Sample Input 1:

# 8 11
# Sample Output 1:

# not enough

def check_sum(*args: int):
    sum = 0
    for i in args:
        sum += i
    if sum < 50:
        print('not enough')
    else:
        print('verification passed')

check_sum(8, 11, 100)