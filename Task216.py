# Проверьте, является ли двумерный массив симметричным относительно главной диагонали. Главная диагональ — та, которая идёт из левого верхнего 
# угла двумерного массива в правый нижний.
# Входные данные
# Программа получает на вход число n<100, являющееся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по n чисел, 
# являющихся элементами массива.
# Выходные данные
# Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.
# Решение задачи Youtube Patreon Boosty
# Sample Input 1:
# 3
# 0 1 2
# 1 5 3
# 2 3 4
# Sample Output 1:
# Yes

N = int(input())
a = []

for i in range(N):
    a.append(list(map(int, input().split())))

down = []
up = []
for i in range(N):
    for j in range(N):
        if i > j:
            up.append(a[i][j])

for j in range(N):
    for i in range(N):
        if i < j:
            down.append(a[i][j])
   
result = True
for i in range(len(down)):
    if down[i] == up[i]:
        result = True
        continue
    else:
        result = False
        break

if result == True:
    print('Yes')
else:
    print('No')