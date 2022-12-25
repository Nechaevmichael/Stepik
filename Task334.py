# Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка. Функция generate_fizz_buzz_list должна
# обойти числа от 1 до n включительно и каждое такое число проверить последовательно на п2 - п5
# Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz 
# Если число кратно трем, то в список заносим строку Fizz
# Если число кратно пяти, то в список заносим строку Buzz
# Если число не кратно ни трем ни пяти, то в список заносим само это число
# В итоге функция generate_fizz_buzz_list должна вернуть сформированный список из n элементов. Ниже показаны примеры вызова:
# generate_fizz_buzz_list(3)  => [1, 2, 'Fizz']
# generate_fizz_buzz_list(7)  => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7]
# generate_fizz_buzz_list(15) => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
# Ваша задача написать только определение функции generate_fizz_buzz_list
# Sample Input 1:
# 4
# Sample Output 1:
# [1, 2, 'Fizz', 4]

def generate_fizz_buzz_list(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        elif i % 3 != 0 and i % 5 != 0:
            result.append(i)
    return result

print(generate_fizz_buzz_list(7))