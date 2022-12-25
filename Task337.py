# Напишите функцию first_unique_char, которая принимает строку символов и возвращает целое число: позицию первого уникального символа в строке. 
# В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.
# Ваша задача написать только определение функции first_unique_char
# Sample Input 1:
# python
# Sample Output 1:
# 0
# Sample Input 2:
# abracadabra
# Sample Output 2:
# 4

def first_unique_char(string):
    position = 0
    for i in range(len(string)):
        if string.count(string[i]) == 1:
            position = i
            break
        else:
            position = - 1
    return position

print(first_unique_char('abcabc'))