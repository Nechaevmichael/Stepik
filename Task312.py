# Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.
# Входные данные
# Входная строка может содержать содержит цифры, пробелы и латинские буквы.
# Выходные данные
# Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной 
# строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.
# Sample Input 1:
# abc12cd34ef35
# Sample Output 1:
# 3

text = input()
numbers = []
for i in text:
    if i.isdigit():
        numbers.append(int(i))
result = []
for i in numbers:
    if numbers.count(i) > 1:
        if i not in result:
            result.append(i)
result = sorted(result)
if len(result) > 0:
    print(*result)
else:
    print('NO')

