# Даны два списка чисел.

# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

# Sample Input:

# 1 3 2 5
# 4 3 2 6
# Sample Output:

# 2 3

list_1 = set(map(int, input().split()))
list_2 = set(map(int, input().split()))

result = sorted(list_1.intersection(list_2))
print(*result)
