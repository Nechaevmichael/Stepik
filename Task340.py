# В этой задаче вам необходимо воспользоваться уже готовой функцией factorial, которая принимает неотрицательное число, 
# и возвращает значение факториала данного числа.
# Ваша задача создать функцию trailing_zeros, которая принимает неотрицательное число, находит его факториал и возвращает 
# сколько нулей на конце этого факториала .
# trailing_zeros(6) =>  1, потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# trailing_zeros(10) => 2, потому что 10! = 3 628 800
# trailing_zeros(20) => 4, потому что 20! = 2 432 902 008 176 640 000
# Нужно написать только определение функций trailing_zeros и factorial

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def trailing_zeros(n):
    count = 0
    number = factorial(n)
    while number != 0:
        if number % 10 == 0:
            count += 1
            number //= 10
        else:
            break
    return count
print(trailing_zeros(20))