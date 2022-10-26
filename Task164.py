# Программа получает на вход натуральное число n > 1. Выведите минимальный делитель этого числа, отличный от единицы.

# К примеру для числа 12 делителями являются 1, 2, 3, 4, 6, 12.

# Sample Input 1:

# 12
# Sample Output 1:

# 2

# s = int(input())
# x = 2
# while s % x != 0:
#     x += 1
# print(x)

n = int(input())
i = 1
count = []
while i <= n:
    if n % i == 0:
        count.append(i)
    i += 1
print(count[1])
