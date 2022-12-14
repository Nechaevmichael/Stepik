# Рассмотрим таблицу из n строк и n столбцов. Известно, что в клетке, образованной пересечением i-й строки и j-го
# столбца, записано число i × j. Строки и столбцы нумеруются с единицы.
# Дано целое положительное число x. Требуется посчитать количество клеток таблицы, в которых находится число x.
# Входные данные
# В единственной строке находятся числа n и x (1 ≤ n ≤ 105, 1 ≤ x ≤ 109) — размер таблицы и число,
# которое мы ищем в таблице.
# Выходные данные
# Выведите единственное число: количество раз, которое число x встречается в таблице.
# Sample Input 1:
# 10 5
# Sample Output 1:
# 2

n, x = map(int, input().split())
a = []
count = 0
for i in range(n):
    a.append([0] * n)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        a[i - 1][j - 1] = i * j

for i in range(n):
    for j in range(n):
        if a[i][j] == x:
            count += 1

print(count)
