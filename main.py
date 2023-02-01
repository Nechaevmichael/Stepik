# ИМПОРТ СОБСТВЕННЫХ БИБЛИОТЕК

# import math_func
# from pprint import pprint

# pprint(dir(math_func))

# print(math_func.get_cube(3))
# print(math_func.get_square(7))


# from math_func import get_square, get_cube

# print(get_square(4))
# print(get_cube(5))

# ПОИСК ФАЙЛА МОДУЛЯ В УКАЗАННОМ СПИСКЕ

# from pprint import pprint
# import sys
# pprint(sys.path)

# ЗАПУСК ИМПОРТИРУЕМОГО ФАЙЛА

# import math_func

# print('Запуск файла main')

# ДЛЯ ПОВТОРНОГО ЗАПУСКА ИМПОРТИРУЕМОГО ФАЙЛА НЕОБХОДИМО ИМПОРТИРОВАТЬ importlib,
# ВНУТРИ КОТОРОГО ЕСТЬ ФУНКЦИЯ reload

# import importlib
# importlib.reload(math_func)

# __name__ and __main__

# import math_func
# print(__name__)

import module_1

if __name__ == '__main__':
    print(__name__)