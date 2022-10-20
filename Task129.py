# Классическая задача для начинающих. 

# Ваша программа должна считать одно натуральное число, после чего вывести:

# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.
# Sample Input 1:

# 15
# Sample Output 1:

# FizzBuzz

number = int(input())

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)

