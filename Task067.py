# На вход программе поступает строка, ваша задача вывести на экран индекс последней найденной латинской буквы "a"

# Если такого символа в введенной строке нет, выведите -1

# Sample Input 1:

# banana
# Sample Output 1:

# 5

text = input()
result = text.rfind('a')
print(result)