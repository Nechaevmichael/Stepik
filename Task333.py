# Напишите функцию factorial, которая принимает на вход одно неотрицательное число, и возвращает значение факториала данного числа.

# Нужно написать только определение функции factorial

# factorial(3) => 6
# factorial(1) => 1
# factorial(0) => 1
# factorial(5) => 120

# # знак => обозначает return
# Sample Input 1:

# 4
# Sample Output 1:

# 24

def factorial(number):
    pr = 1
    for i in range(2, number + 1):
        pr *= i
    return pr

print(factorial(5))