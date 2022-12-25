# Ваша задача написать функцию format_name_list, которая принимает список словарей, у каждого словаря в этом списке есть только ключ name.

# Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и". 
# Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:

# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) => 'Bart, Lisa и Maggie'

# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) => 'Bart и Lisa'

# format_name_list([{'name': 'Bart'}]) => 'Bart'

# format_name_list([]) => ''
# Ваша задача написать только определение функции format_name_list

def format_name_list(names: list[dict]) -> str:
    result = []
    for i in range(len(names)):
        result.append(names[i]['name'])
    result_str = ''
    if len(result) == 0:
        return result_str
    elif len(result) == 1:
        return f'{result[0]}'
    elif len(result) == 2:
        return f'{result[0]} и {result[1]}'
    elif len(result) > 2:
        temp = ', '.join(result[:-2])
        return f'{temp}, {result[-2]} и {result[-1]}'


print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))