# Напишите программу, которая проверяет, чтобы введенная фраза s одновременно начиналась со строки prefix и 
# заканчивалась строкой postfix 
# Входные данные
# В отдельных строках вводится три значения: сперва строка s, затем строка prefix и потом postfix
# Выходные данные
# Нужно вывести True, если введенная строка s одновременно начинается со строки prefix и заканчивается строкой postfix . 
# Во всех остальных случаях нужно вывести False. Регистр букв нужно учитывать
# Sample Input 1:
# translate russian to english
# translate
# english
# Sample Output 1:
# True

text = input()
start = input()
end = input()
if text.startswith(start) == True and text.endswith(end) == True:
    print(True)
else:
    print(False)