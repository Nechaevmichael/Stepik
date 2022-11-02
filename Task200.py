# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20.
    
sum_4 = 0

for i in range(1000, 10000):
    number = i
    sum = 0
    while i > 0:
        sum += i % 10
        i //= 10
    if sum == 20:
        sum_4 += number

print(sum_4)