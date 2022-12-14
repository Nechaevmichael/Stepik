# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем считается тот спортсмен, у 
# которого сумма результатов по всем броскам максимальна.
# Если перенумеровать спортсменов числами от 0 до n-1, а попытки каждого из них – от 0 до m-1, то на вход программа 
# получает массив A[n][m], состоящий из неотрицательных целых чисел. Программа должна определить максимальную сумму 
# чисел в одной строке и вывести на экран эту сумму и номер строки, для которой достигается эта сумма.
# Входные данные
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке 
# идет n строк по m чисел, являющихся элементами массива.
# Выходные данные
# Программа должна вывести  2 числа: сумму и номер строки, для которой эта сумма достигается. Если таких строк несколько, 
# то выводится номер наименьшей из них. Не забудьте, что нумерация строк (спортсменов) начинается с 0.
# Sample Input:
# 2 2
# 5 4
# 3 5
# Sample Output:
# 9
# 0

a = []
N, M = map(int, input().split())

for i in range(N):
    a.append(list(map(int, input().split())))
b = []
for i in range(N):
    sum = 0
    for j in range(M):
        sum += a[i][j]
    b.append(sum)
result = max(b)
print(result)
for i in range(len(b)):
    if b[i] == result:
        print(i)