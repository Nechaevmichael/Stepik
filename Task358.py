# Определите функцию print_to, которая принимает одно натуральное число n и распечатывает на экране последовательность целых чисел от 1 до n включительно. 
# Каждое число необходимо выводить на отдельной строке. 
# Ваша задача только написать определение функции print_to
# Sample Input 1:
# 5
# Sample Output 1:
# 1
# 2
# 3
# 4
# 5
number = 1
def print_to(n: int):
    global number
    if number <= n:
        print(number)
        number += 1
        return print_to(n)

print_to(5)