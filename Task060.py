# Программа получает на вход строку.

# Выведите каждый третий символ строки в обратном порядке, начиная с последнего.

# Sample Input:

# The Big Bang Theory
# Sample Output:

# ye ag T

text = input()
print(text[-1::-3])