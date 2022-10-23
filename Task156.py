# Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа

# Sample Input 1:

# 415
# Sample Output 1:

# 20

number = int(input())
result = 1
while number > 0:
    result *= number % 10
    number //= 10
print(result)