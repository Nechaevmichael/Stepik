# Проверка данных на тип

value = [1, 2, 3]

match value:
    case int() | float():
        print('Число')
    case str():
        print('Строка')
    case list():
        print('Список')
    case _:
        print('Не понятно что это!')
