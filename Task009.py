# Напишите программу, которая вычисляет длину отрезка (т.е. расстояние между двумя точками),
#  заданного двумя значениями x1 и x2 (вещественные числа).
# 🚀>P.S.: Подсказка для решения 🚀
# Sample Input 1:
# -2 6.5
# Sample Output 1:
# 8.5

a, b = map(float, input().split())

res = (abs(b - a))
print(res)