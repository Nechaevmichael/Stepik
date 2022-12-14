# Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.

# Под главной диагональю матрицы подразумевается диагональ, проведённая из левого верхнего угла в правый нижний.

# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, а затем в N строках записаны элементы списка.

# Sample Input 1:

# 2
# 1 2
# 3 4
# Sample Output 1:

# 5

matrix = []
N = int(input())
sum = 0
for i in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i == j:
            sum += matrix[i][j]


print(sum)