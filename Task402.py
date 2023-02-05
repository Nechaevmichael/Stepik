# В этой задаче вам необходимо скачать файл (numbers.txt), в котором записаны натуральные числа. Ваша задача найти
# количество трехзначных чисел;
# сумму двухзначных чисел
# В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов. Сперва количество, потом сумма

def count_numbers(file_name: str) -> int:
    data = open(file_name, 'r', encoding='utf-8')
    current_numbers = 0
    sum_numbers = 0

    for i in data:
        if len(i) == 4:
            current_numbers += 1
        if len(i) == 3:
            sum_numbers += int(i)

    print(current_numbers, sum_numbers)



count_numbers('numbers.txt')