# Для каждого вопроса в отдельной строчке через пробел выведите имена всех одноклассников, которые родились в указанном месяце. 
# Имена упорядочьте в лексикографическом порядке.
# Если в заданном месяце никто не родился, выведите сообщение "Нет данных".
# Sample Input:
# 4
# Саша 20 янв
# Артем 15 июн
# Карл 10 янв
# Коля 20 июл
# 3
# июн
# дек
# янв
# Sample Output:
# Артем
# Нет данных
# Карл Саша

n = int(input())
birthday = {}

for i in range(n):
    data = input().split()
    if data[2] not in birthday:
        birthday[data[2]] = [data[0]]
    elif data[2] in birthday:
        birthday[data[2]].append(data[0])
        birthday[data[2]].sort()

m = int(input())
for i in range(m):
    month = input()
    if month in birthday:
        print(*birthday[month])
    else:
        print('Нет данных')