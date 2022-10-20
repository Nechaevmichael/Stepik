# Программа определяет наименование месяца по его номеру n. Название месяца пишется с заглавной буквы

# Программа получает на вход номер месяца - натуральное число N (N<=12) и в зависимости от его значения вывод название месяца 

# Sample Input 1:

# 4
# Sample Output 1:

# Апрель

month = int(input())
if month == 1:
    print('Январь')
elif month == 2:
    print('Февраль')
elif month == 3:
    print('Март')
elif month == 4:
    print('Апрель')
elif month == 5:
    print('Май')
elif month == 6:
    print('Июнь')
elif month == 7:
    print('Июль')
elif month == 8:
    print('Август')
elif month == 9:
    print('Сентябрь')
elif month == 10:
    print('Октябрь')
elif month == 11:
    print('Ноябрь')
else:
    print('Декабрь')