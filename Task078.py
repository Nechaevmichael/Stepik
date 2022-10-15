# Теперь ваша программа спрашивает у пользователя не только имя, но и его возраст.
# После этого программа должна вывести сообщение:
# "Hello <name>. You are <age> years old."
# Обратите внимание, что буквы в имени все должны быть заглавные. И не забывайте пользоваться f-строкой
# Sample Input:
# Messi
# 33
# Sample Output:
# Hello MESSI. You are 33 years old.

name = input('Введите Ваше имя: ')
age = input('Введите Ваш возраст: ')
print(f'Hello {name.upper()}. You are {age} years old.')