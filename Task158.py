# Программа принимает на вход одно натуральное число. Ваша задачи найти сколько раз встречается цифра 7 в этом числе

# Sample Input 1:

# 777
# Sample Output 1:

# 3

number = int(input())
count = 0
while number > 0:
    last_digit = number % 10
    if last_digit == 7:
        count += 1
    number //= 10
print(count)