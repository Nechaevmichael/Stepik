# Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).
# Входные данные
# Программа получает на вход два числа n и m.
# Выходные данные
# Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.
# Sample Input 1:
# 4 10
# Sample Output 1:
# 0  1  2  3  4  5  6  7  8  9
# 19 18 17 16 15 14 13 12 11 10
# 20 21 22 23 24 25 26 27 28 29
# 39 38 37 36 35 34 33 32 31 30

a = []
count = 0
n, m = map(int, input().split())

for i in range(n):
    a.append([0] * m)

for i in range(n):
    for j in range(m):
        a[i][j] = count
        count += 1

for i in range(n):
    if i % 2 == 0:
        continue
    else:
        a[i].sort(reverse=True)

for i in a:
    print(*i)


# for i in range(n):
#     tmp = []
#     if i % 2 == 0:
#         for j in range(m):
#             tmp.append(count)
#             count += 1
#         a.append(tmp)
#     else:
#         for j in range(m):
#             tmp.append(count)
#             count += 1
#         a.append(tmp[::-1])
# for i in a:
#     print(i)
