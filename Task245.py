# В вашем распоряжении список numbers. ​Ваша задача удалить из этого списка числа 3, 5, 7 и 9. 

#  В качестве ответа необходимо вывести измененный список numbers

numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]

numbers.remove(3)
numbers.remove(5)
numbers.remove(7)
numbers.remove(9)
print(numbers)

# В вашем распоряжении список numbers. Ваша задача отсортировать список numbers в порядке убывания  и вывести на экран результат.

# Sample Input:

# Sample Output:

# [472, 448, 422, 284, 198, 181, 32, 29, -20, -139, -214, -895, -917, -964, -986, -989]

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]

numbers.sort(reverse=True)
# print(numbers[::-1])

print(numbers)

# В вашем распоряжении списков numbers. Ваша задача скопировать все содержимое списка numbers в новую переменную copy_numbers

#  В качестве ответа необходимо вывести измененный список copy_numbers

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers_copy = numbers.copy()
print(numbers_copy)