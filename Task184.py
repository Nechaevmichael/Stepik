# Напишите программу, которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.

# Формат ввода
# Вводится одна строка.

# Формат вывода
# Выводится одно целое число — максимальное количество раз, которое встречается какая-либо буква (без учёта регистра) 
# или иной символ во введённой строке.

# Sample Input 1:

# Сокол
# Sample Output 1:

# 2

text = input().lower()
L = []

for i in range(len(text)):
    count = 0
    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1
    L.append(count)
print(max(L))