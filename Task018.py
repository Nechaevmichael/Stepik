# Напишите программу, которая найдет сколько полных килограмм умещается в заданное число грамм.

# Формат входных данных
# На вход программе подаётся натуральное число – количество грамм.

# Формат выходных данных
# Программа должна вывести одно число – полное число килограмм .

#  1кг = 1000г
# Sample Input:

# 3456
# Sample Output:

# 3
weight = int(input("Введите количество грамм: "))
result = weight // 1000
print(result)