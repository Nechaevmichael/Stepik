# Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого 
# из моментов времени. Известно, что второй момент времени наступил не раньше первого. 
# Определите, сколько секунд прошло между двумя моментами времени.
# Входные данные
# Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и три 
# целых числа, задающих второй момент времени.
# Выходные данные
# Выведите число секунд между этими моментами времени.
# 🚀>P.S.: Подсказка для решения 🚀
# Sample Input 1:
# 1
# 1
# 1
# 2
# 2
# 2
# Sample Output 1:
# 3661

hour_1 = int(input())
min_1 = int(input())
sec_1 = int(input())
hour_2 = int(input())
min_2 = int(input())
sec_2 = int(input())

res = 3600 * (hour_2 - hour_1) + 60 * (min_2 - min_1) + (sec_2 - sec_1)
print(res)