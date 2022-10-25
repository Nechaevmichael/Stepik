# На каждой отдельной строчке пользователь вводит друг за другом пароли в виде строки символов. 
# Валидными паролями будем считать строки, у которых длина варьируется от 5 до 9 символов включительно. 
# Как только вы встретите первый невалидный пароль, ваша программа должна закончить считывать пароли и 
# вывести последний введенный валидный пароль.
# Гарантируется, что первый пароль всегда валидный
# Sample Input 1:
# QWERTY
# 12345
# 21.08.90
# Кодзима-гений
# Телепузик
# Sample Output 1:
# 21.08.90
# result = ''
# while True:
#     password = input()
#     if len(password) >= 5 and len(password) <= 9:
#         result = password
#     else:
#         break
# print(result)
result = ''
text = input()
while len(text) >= 5 and len(text) <= 9:
    result = text
    text = input()
    if len(text) < 5 and len(text) > 9:
        break
print(result)