# Напишите программу, которая считывает слово, затем выводит:

# «Что Вы сказали? [это слово] ? Какое интересное слово».

# Sample Input 1:

# Конвульсия
# Sample Output 1:

# Что Вы сказали? Конвульсия? Какое интересное слово

word = input()
result = '"Что Вы сказали? {word}? Какое интересное слово".'.format(word = word)
print(result)