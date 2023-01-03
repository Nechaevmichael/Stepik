# Описать рекурсивную функцию tribonacci, которая принимает на вход целое число n - порядковый номер чисел Трибоначчи.
# Функция по параметру n должна вычислить и вернуть значение,
# стоящее на n-м месте в ряде чисел Трибоначчи
# Вот примеры вызовов:

# tribonacci(0) => 0
# tribonacci(2) => 1
# tribonacci(4) => 2
# tribonacci(6) => 7
# tribonacci(7) => > 13
# Ваша задача только написать определение функции tribonacci

# lst_Tribonacci = [0, 0, 1]
# def tribonacci():
#     if len(lst_Tribonacci) <= 30:
#         lst_Tribonacci.append(lst_Tribonacci[-3] + lst_Tribonacci[-2] + lst_Tribonacci[-1])
#         return tribonacci()
# tribonacci()
# a = int(input())
# print(lst_Tribonacci[a])

n = int(input())
def fib(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2) + fib(n-3)

print(fib(n))