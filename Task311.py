# Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, 
# но при этом отсутствуют во втором. 
# Sample Input:
# 1 3 2 5
# 4 3 2 6
# Sample Output:
# 1 5

list_1 = set(map(int, input().split()))
list_2 = set(map(int, input().split()))

result = sorted(list_1.difference(list_2))
print(*result)