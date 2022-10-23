# Программа принимает на вход одно натуральное число и выводит его цифры в столбик в обратном порядке.

# Sample Input 1:

# 412
# Sample Output 1:

# 2
# 1
# 4

number = int(input())
while number > 0:
    print(number % 10)
    number //= 10