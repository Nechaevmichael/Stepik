# Найди факториал числа n

fact = 1
n = int(input())

for i in range(2, n + 1):
    fact *= i
print(fact)