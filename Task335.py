# В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b), которая принимает два числа и находит наибольших общий делитель для них.
# Ваша задача при помощи функции gcd определить НОД произвольного количества чисел.
# Входные данные
# На первой строке вводится натуральное число n – количество чисел. Далее идут n строк, в каждой из которых натуральное число.
# Выходные данные
# НОД введенных чисел.
# Sample Input 1:
# 3
# 15
# 18
# 27
# Sample Output 1:
# 3

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def res():
    count_numbers = int(input())
    result = []
    for i in range(count_numbers):
        temp = int(input())
        result.append(temp)
    return gcd(min(result), max(result))

print(res())
