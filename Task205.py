# Отсортировать пузырьковым методом.

n = int(input()) # количество элементов в списке

mas = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    for j in range(n - 1):
        if mas[j] > mas[j + 1]:
             mas[j], mas[j + 1] = mas[j + 1], mas[j]
             count += 1
print(*mas)
print(count)