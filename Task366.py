# Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из списков, 
# внутри которых также могут быть списки. Ваша задача превратить все это в линейный список при помощи функции flatten

# flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
# flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
# flatten([[[[9]]], [1, 2], [[8]]]) => [9, 1, 2, 8]
# Ваша задача только написать определение функции flatten

def flatten(lst: list, result_list: list=None):
    if result_list is None:
        result_list = []
    for i in lst:
        if type(i) == list:
            flatten(i, result_list)
        else:
            result_list.append(i)
    return result_list

print(flatten([[[[9]]], [1, 2], [[8]]]))