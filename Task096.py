# Программа получает на вход список целых чисел и ваша задача вывести второй элемент этого списка.

# Гарантируется, что список будет состоять не менее чем из трех элементов

# Примечание:

# Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку

# a = list(map(int, input().split()))
# Sample Input 1:

# 8 11 19 200
# Sample Output 1:

# 11

my_list = list(map(int, input().split()))
print(my_list[1])