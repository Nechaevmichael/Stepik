# Программа принимает на вход два целых числа a и b.

# Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно и вывести его на экран.

# Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно, двигаясь в порядке убывания, и затем вывести его.

# Не забывайте пользоваться генератором списков 

# Sample Input 1:

# 1 5
# Sample Output 1:

# [1, 4, 9, 16, 25]

a, b = map(int, input().split())

if a <= b:
    c = [i ** 2 for i in range(a, b + 1)]
else:
    c = [i ** 3 for i in range(a, b - 1, - 1)]

print(c)