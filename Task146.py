# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.

# Задано единственное целое число N

# Необходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа N.

# Sample Input 1:

# 15
# Sample Output 1:

# 1
# 4
# 9

N = int(input())
i = 1
while i**2 <= N:
    print(i*i)
    i += 1
