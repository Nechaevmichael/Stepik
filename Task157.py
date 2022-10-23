# Программа принимает на вход одно натуральное число и выводит на экран минимальную и 
# максимальную цифры данного числа в отдельных строчках

# Sample Input 1:

# 480
# Sample Output 1:

# 0
# 8

number = int(input())
min = 9
max = 0
while number > 0:
    last_digit = number % 10
    if last_digit < min:
        min = last_digit
    if last_digit > max:
        max = last_digit
    number //= 10
print(min)
print(max)