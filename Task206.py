# Программа получает на вход число n - количество элементов в списке, и затем в следующей строке сам список.

# Ваша задача отсортировать список по возрастанию при помощи сортировки вставками, в случае если элементы соседние совпадают менять их ненужно.

# В качестве ответа нужно вывести отсортированный список.

# Sample Input 1:

# 6
# 5 4 2 15 6 6
# Sample Output 1:

# 2 4 5 6 6 15
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j -1], a[j]
        else:
            break
print(*a)