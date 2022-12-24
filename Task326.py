# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

# Сложным паролем будет считаться комбинация символов, в которой :

# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква 
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"

# Вам необходимо написать только определение функции check_password

def check_password(password):
    length = len(password)
    digit = 3
    upper = False
    symbol = False
    for i in password:
        if i.isdigit():
            digit -= 1
        if i != i.lower():
            upper = True
        if i in '!@#$%*':
            symbol = True
    if length >= 10 and digit <= 0 and upper == True and symbol == True:
        print('Perfect password')
    else:
        print('Easy peasy')

check_password('Qwert1357!')
