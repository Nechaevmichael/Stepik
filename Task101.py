# Перед вами находится список months, хранящий сокращенное название месяцев в году

# Ваша программа получает на вход порядковый номер месяца в году - целое число от 1 до 12.

# Ваша задача распечатать кратное название месяца, которое соответствует порядковому номеру месяца

# Sample Input 1:

# 1
# Sample Output 1:

# Jan

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month = int(input())
print(months[month - 1])