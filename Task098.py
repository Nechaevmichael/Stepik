# Программа получает на вход список целых чисел и ваша задача вывести последние три элемента этого списка через срез

# Гарантируется, что список будет состоять не менее чем из пяти элементов.

# Примечание:

# Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной a вам необходимо написать строчку

# a = list(map(int, input().split()))
# Sample Input:

# 89 45 7 33 65 12
# Sample Output:

# [33, 65, 12]

my_list = list(map(int, input().split()))
print(my_list[-3:])