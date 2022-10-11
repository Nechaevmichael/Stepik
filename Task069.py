# Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.

# Ваша задача заменить все пробелы запятыми и вывести полученную строку.

# Sample Input:

# Smells Like Teen Spirit
# Sample Output:

# Smells,Like,Teen,Spirit

text = input()
print(text.replace(' ', ','))
