# На вход программе поступает целое число

# Ваша задача сохранить в переменную text  строку Even, если введенное число четное, иначе сохраните строку Odd

# В качестве ответа необходимо вывести переменную text

# Sample Input 1:

# 8
# Sample Output 1:

# Even

number = int(input())

text = 'Even' if number % 2 == 0 else 'Odd'

print(text)