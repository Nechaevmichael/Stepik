# В последний день уходящего 2016 года Лимак собирается принять участие в соревновании по спортивному программированию. 
# Соревнование начнётся в 20:00 и будет продолжаться четыре часа, то есть ровно до полуночи. Участникам будет предложено n задач, 
# упорядоченных по возрастанию сложности, то есть задача 1 будет самой лёгкой, а задача номер n — самой сложной. Лимак знает, 
# что ему потребуется 5·i минут на решение i-й задачи.
# Друзья Лимака планирую устроить роскошную новогоднюю вечеринку и Лимак хочет прибыть в полночь или ранее. 
# Он знает, что ему требуется ровно k минут чтобы добрать до места проведения вечеринки от своего дома, где он 
# собирается участвовать в соревновании.
# Сколько максимум задач может успеть решить Лимак, так чтобы не опоздать на новогоднюю вечеринку?
# Входные данные
# В первой строке входных данных записаны два целых числа n и k (1 ≤ n ≤ 10, 1 ≤ k ≤ 240) — количество задач в соревновании и количество минут, 
# за которое Лимак доберётся от дома до места проведения вечеринки.
# Выходные данные
# Выведите одно целое число, равное максимальному количеству задач, которое может решить Лимак, так чтобы 
# прибыть на новогоднюю вечеринку ровно в полночь или раньше.

count_task, time_to_party = map(int, input().split()) # Количество задач в соревновании

# time_to_party = int(input()) # Время необходимое для того, чтобы добраться до вечеринки

time = 0 # Время необходимое для решения задач

count_task_result = 0

all_time = 240

for i in range(0, count_task):
    time += 5
    all_time -= time
    # result = all_time - time
    count_task_result += 1
    if all_time >= time_to_party:
        continue
    else:
        count_task_result -= 1
        break
print(count_task_result)
