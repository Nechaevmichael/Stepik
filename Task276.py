# Напишите программу, которая печатает словарь alphabet, где ключи  - строчные английские символы, а значения - порядковые номера букв в алфавите начиная с 1.

# Начало вашего словаря должны быть таким {"a": 1, "b": 2 ... }

# В качестве ответа распечатайте полученный словарь alphabet

# Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:

from string import ascii_lowercase
# print(ascii_lowercase)

alphabet = {}

for i in range(1, 27):
    alphabet[ascii_lowercase[i - 1]] = i
print(alphabet)