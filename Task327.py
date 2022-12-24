# Создайте функцию count_letters, которая принимает на вход фразу и подсчитывает, какое количество в ней строчных(K) 
# и заглавных (N) букв, все остальные символы игнорируются. Функция должна вывести на экран информацию о найденных буквах в определенном формате. 
# Количество заглавных символов: N
# Количество строчных символов: K
# Вам необходимо написать только определение функции count_letters.

# from string import ascii_uppercase
# from string import ascii_lowercase

# def count_letters_1(text):
#     count_upper = 0
#     count_lower = 0
#     for i in text:
#         if i in ascii_lowercase:
#             count_lower += 1
#         elif i in ascii_uppercase:
#             count_upper += 1
#     print(f'Количество заглавных симоволов: {count_upper}')
#     print(f'Количество строчных символов: {count_lower}')

# count_letters_1('QWERTYqwerty')

def count_letters(text):
    count_upper = 0
    count_lower = 0
    for i in text:
        if i.isalpha() and i == i.upper():
            count_upper += 1
        elif i.isalpha() and i == i.lower():
            count_lower += 1
    print(f'Количество заглавных символов: {count_upper}')
    print(f'Количество строчных символов: {count_lower}')

count_letters('Privet')