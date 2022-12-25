# Давайте считать человека подростком, если его возраст находится в пределах от 12 до 17 лет. 
# Напишите функцию is_person_teenager , которая помогает по возрасту определить является ли человек подростком или нет.
# Функция is_person_teenager принимает на вход возраст человека и возвращает True или False
# Нужно написать только определение функций is_person_teenager 
# Sample Input 1:
# 8
# Sample Output 1:
# False

def is_person_teenager(age):
    return age >= 12 and age <= 17

print(is_person_teenager(12))