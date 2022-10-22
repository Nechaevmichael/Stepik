# Введите пароль

guess = input()
password = 'qwerty'

while guess != password:
    print('Не верный пароль! \nВведите ещё раз: ')
    guess = input()
print('Верно!')