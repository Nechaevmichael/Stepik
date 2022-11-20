# При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита ['A', 'B', 'C', 'D', ...]. 
# Получить все заглавные буквы английского алфавита можно следующим образом:
# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Входные данные
# На вход программе подается натуральное число n, n≤26.
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита
# Sample Input 1:
# 3
# Sample Output 1:
# ['A', 'B', 'C']
from string import ascii_uppercase
n = int(input())

a = [ascii_uppercase[i] for i in range(n)]
print(a)

# Давайте усовершенствуем предыдущую задачу так, чтобы получался следующий список букв:
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]

b = [ascii_uppercase[i] * (i + 1) for i in range(n)]
print(b)