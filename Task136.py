# Часто можно услышать такой вопрос. Давайте это запрограммируем.
# Программа получает на вход номер месяца - натуральное число N (1<= N <=12) и в зависимости от его 
# значения выводит количество дней в месяце. Будем считать, что год невисокосный. 
# При решении конечно же используйте оператор match-case
#  Cколько дней в каком месяце
# Январь - 31 день
# Февраль - 28 дней
# Март - 31 день
# Апрель - 30 дней
# Май - 31 день
# Июнь - 30 дней
# Июль - 31 день
# Август - 31 день
# Сентябрь - 30 дней
# Октябрь - 31 день
# Ноябрь - 30 дней
# Декабрь - 31 день
# Sample Input 1:
# 1
# Sample Output 1:
# 31

month = int(input())
match month:
    case 1:
        print(31)
    case 2:
        print(28)
    case 3:
        print(31)
    case 4:
        print(30)
    case 5:
        print(31)
    case 6:
        print(30)
    case 7:
        print(31)
    case 8:
        print(31)
    case 9:
        print(30)
    case 10:
        print(31)
    case 11:
        print(30)
    case 12:
        print(31)