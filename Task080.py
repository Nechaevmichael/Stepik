# Напишите программу для перевода натурального значения секунд в значение минут определенного формата.

# Sample Input 1:

# 99
# Sample Output 1:

# 99 сек - это 1 мин. 39 сек.

time = int(input("Введите значение секунд: "))
print(f'{time} секунд - это {time // 60} мин. {time % 60} сек.')