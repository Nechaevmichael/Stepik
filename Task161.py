# Программа получает на вход натуральное число N. 

# Нужно найти сумму его делителей. 

# Sample Input 1:

# 10
# Sample Output 1:

# 18

number = int(input())
i = 1
sum = 0
while i <= number:
    if number % i == 0:
        sum += i
    i += 1
print(sum)