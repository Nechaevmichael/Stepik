# Напишите функцию count_letter(text, letter), которая принимает два параметра:

# text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
# letter – буква, количество которой мы должны посчитать в text.
# Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text

# Ваша задача дописать только тело функции count_letter

def count_letter(text, letter):
    count = 0
    for i in text:
        if i == letter:
            count += 1
    print(count)

a = 'to be or not to be'
b = 'b'
count_letter(a, b)