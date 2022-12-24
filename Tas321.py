# Всеми любимая программа «hello world». Создайте функцию с именем say_hello_world , которая принимает на вход имя человека в виде 
# строки и печатает фразу «{name} говорит hello world!»

# Ваша задача написать только определение функции say_hello_world

name = input()

def say_hello_world(x):
    print(f'{x} говорит hello world!')

say_hello_world(name)