# Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.

# Учитывайте, что содержимое файла может быть как на русском языке, так и на английском

def file_read(file_name):
    file_1 = open(file_name, 'r', encoding='utf-8')
    print(file_1.read())

file_read(file_2)