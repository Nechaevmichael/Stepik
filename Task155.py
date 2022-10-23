# Программа принимает на вход одно натуральное число и выводит на экран сумму цифр данного числа

# Sample Input 1:

# 123
# Sample Output 1:

# 6

number = int(input())
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(sum)