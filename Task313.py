# Напишите программу, которая удаляет из строки все повторяющиеся символы, при этом регистр букв необходимо учитывать.
# Входные данные
# Программа получает на вход строку, состоящую из заглавных и строчных символов, цифр и знаков препинания.
# Выходные данные
# Программа должна вывести исходную строку, из которой удалены все повторяющиеся символы.
# Sample Input 1:
# hello_world!
# Sample Output 1:
# helo_wrd!

text = input()
result = set(text)
for i in text:
    if i in result:
        print(i, end='')
        result.remove(i)

