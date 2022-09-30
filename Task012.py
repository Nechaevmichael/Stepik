# Вводится вещественное число и нам нужно его округлить до 2 и 3 разряда после запятой и вывести полученный 
# результат через пробел в одной строчке

# Sample Input 1:

# 0.123456789
# Sample Output 1:

# 0.12 0.123

number = float(input())
number_1 = round(number, 2)
number_2 = round(number, 3)
print(number_1, number_2)