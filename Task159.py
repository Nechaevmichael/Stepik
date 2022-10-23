# Программа принимает на вход одно натуральное число и выводит его цифры в двоичной системе в столбик в обратном порядке.

# Sample Input 1:

# 8
# Sample Output 1:

# 0
# 0
# 0
# 1

number = int(input())
while number > 0:
    print(number % 2)
    number //= 2