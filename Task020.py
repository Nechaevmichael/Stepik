# Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа

# Sample Input 1:

# 123
# Sample Output 1:

# 6
# Sample Input 2:

# 109
# Sample Output 2:

# 10
number = int(input('Введите число: '))
a = number % 10
b = number // 10 % 10
c = number // 100
print(a + b + c)