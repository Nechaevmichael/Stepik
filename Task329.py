# Напишите функцию is_between, которая принимает три аргумента и печатает True, если первое число находится между двумя вторыми включительно, 
# и False в противном случае.

# Ваша задача дописать только тело функции is_between

def is_between(a, b, c):
    if a <= c and a >= b:
        print(True)
    else:
        print(False)

is_between(9, 9, 9)