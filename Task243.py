# В вашем распоряжении два списка numbers  и extra. Ваша задача расширить numbers список за счет списка extra

# Все элементы списка extra должны добавиться по порядку в конец списка numbers

#  В качестве ответа необходимо вывести измененный список numbers

# Sample Input:

# Sample Output:

# [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29, 43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]

extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]

numbers.extend(extra)
print(numbers)