# Найдите, в каких строках из введённых и в каком месте упоминается "рок", причем регистр букв не важен.
# Вместо явного цикла прохода по строке в цикле используйте подходящий метод строки.
# Формат ввода
# На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк.
# Формат вывода
# Для каждой строки, в которой есть сочетание символов «рок», нужно вывести 
# (в порядке появления таких строк) номер этой строки (нумерация начинается с единицы) и номер символа, 
# с которого начинается первое вхождение этой подстроки (нумерация символов также с единицы).
# Разбор Youtube Patreon Boosty
# Sample Input 1:
# 3
# Порок
# Учитель
# Рок
# Sample Output 1:
# 1 3
# 3 1

N = int(input())

for i in range(N):
    text = input().lower()
    if "рок" in text:
        print(i + 1, text.find('рок') + 1)