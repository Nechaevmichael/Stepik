# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них. 
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов (числа не превышают 1000).
# Разбор решения Youtube Patreon Boosty
# Sample Input 1:
# 5
# 6
# 7
# Sample Output 1:
# 10

import math
class_1 = int(input())
class_2 = int(input())
class_3 = int(input())
count = math.ceil(class_1 / 2) + math.ceil(class_2 / 2) + math.ceil(class_3 / 2)
print(count) 