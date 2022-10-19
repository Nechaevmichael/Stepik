# В отделе работают 3 сотрудника, которые получают заработную плату в рублях. 
# Требуется определить: на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
# Входные данные
# Размеры зарплат всех сотрудников вводятся в одну строку через пробел. Каждая заработная плата – 
# это натуральное число, не превышающее 105. И гарантируется ,что все зарплаты различны
# Выходные данные
# Необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой.
# Примечание: функциями min и max пользоваться нельзя, мы же условный оператор изучаем)
# Sample Input 1:
# 100 500 1000
# Sample Output 1:
# 900

a, b, c = map(int, input().split())
min = 0
max = 0
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c

if a < b:
    if a < c:
        min = a
    else:
        min = c
else:
    if b < c:
        min = b
    else:
        min = c

result = max - min
print(result)