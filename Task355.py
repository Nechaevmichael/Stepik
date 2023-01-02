# Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.

# Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде пары <Ключ> = <Значения>, 
# причем ключи должны следовать в алфавитном порядке. Пример работы смотрите ниже

# info_kwargs(first_name="John", last_name="Doe", age=33) 
# """ данный вызов печатает следующие строки
# age = 33
# first_name = John
# last_name = Doe
# """
# Вам необходимо написать только определение функции

def info_kwargs(**kwargs):
    for i in sorted(kwargs):
        print(f"{i} = {kwargs[i]}")

info_kwargs(first_name="John", last_name="Doe", age=33) 


