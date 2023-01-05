# Быстрая сортировка - еще один вид сортировки, который использует рекурсию. 
# Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию quick_sort, 
# которая будет принимать исходный список и возвращать новый отсортированный в порядке неубывания список.
# Необходимо написать только определение функций quick_sort, при этом нельзя пользоваться встроенными сортировками в Python
# Sample Input 1:
# 5
# 19 4 5 17 1
# Sample Output 1:
# 1 4 5 17 19

# def sort(lst: list) -> list:
#     result_list = []
#     for i in range(len(lst)):
#         result_list.append(min(lst))
#         lst.remove(min(lst))
#     print(result_list)

# sort([1, -2, 10, 3, 24, -222])

def quick_sort(s):
    if len(s) <= 1:
        return s
    
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([7, 6, 10, 5, 9, 8, 3, 4]))