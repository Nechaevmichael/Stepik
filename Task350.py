# Напишите функцию count_args, которая принимает произвольное количество аргументов. Данная функция должна возвращать количество переданных ей на вход аргументов

# count_args(1, 2, 3) => 3
# count_args(1, 3) => 2
# count_args(2) => 1
# count_args() => 0
# Вам необходимо написать только определение функции count_args

def count_args(*args):
    count = 0
    for i in args:
        count += 1
    return count

print(count_args(1, 2, 3, 4, [1, 2, 3]))