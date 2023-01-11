# Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках)
# Ваша задача написать программу, которая находит информацию, кто из актеров получил наибольшее и наименьшее количество статуэток
# Входные данные
# Программа принимать на вход в первой строке натуральное число n - количество вручаемых сегодня наград. 
# И затем в n следующих строках вводятся имена актеров - победителей.
# Выходные данные
# Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток и через запятую их количество. 
# Гарантируется, что всегда будет только один человек, набравших наибольшее и наименьшее количество статуэток.
# Sample Input:
# 6
# Леонардо Ди Каприо
# Джонни Депп
# Леонардо Ди Каприо
# Леонардо Ди Каприо
# Джонни Депп
# Мэтт Деймон
# Sample Output:
# Леонардо Ди Каприо, 3
# Мэтт Деймон, 1

count = int(input())
actors = {}

for i in range(count):
    temp = input()
    if temp in actors:
        actors[temp] += 1
    else:
        actors[temp] = 1

actors = sorted(actors.items(), key= lambda para: para[1], reverse=True)

print(f'{actors[0][0]}, {actors[0][1]} \n{actors[-1][0]}, {actors[-1][1]}')

n = int(input())

actors = {}

for i in range(n):
    actor = input()
    if actor in actors:
        actors[actor] += 1
    else:
        actors[actor] = 1

actor_max = ''
max = 0
actor_min = ''
min = 1000
for key, value in actors.items():
    if value > max:
        max = value
        actor_max = key
    if value < min:
        min = value
        actor_min = key

print(str(actor_max) + ', ' + str(max)) 
print(str(actor_min) + ', ' + str(min))