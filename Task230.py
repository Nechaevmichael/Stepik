# Напишите программу, которая проверяет заканчивается ли введенная фраза s строкой postfix 
# Входные данные
# В отдельных строках вводятся два значения: сперва строка s, затем строка postfix
# Выходные данные
# Нужно вывести True, если введенная строка s заканчивается строкой postfix , во всех остальных 
# случаях нужно вывести False. Регистр букв нужно учитывать
# Sample Input 1:
# привет как дела
# дела
# Sample Output 1:
# True
s = input()
postfix = input()

print(s.endswith(postfix))