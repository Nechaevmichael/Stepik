# file = open(r'C:\Users\Михаил\Desktop\Stepik\work_with_files\111.txt', encoding='utf-8')
# print(file.read(2))
# print(file.read(2))
# print(file.read(2))
# file.seek(0)
# print(file.read(2))
# print(file.readline())
# file.seek(0)
# print('-' * 20)
# print(file.readline())

# for string in file:
#     print(string)
#     for letter in string:
#         print(letter, end=' ')
# file.seek(0)
# print('-' * 20) #  
# s = file.readlines()
# print(s) # ['После команды push будет предложено оформить pull request пройдя по \n', 'ссылке.\n', "Когда страница откроется. останется просто нажать: 'Create pull request'"]

file = open(r'C:\Users\Михаил\Desktop\Stepik\work_with_files\111.txt', 'a', encoding='utf-8')
file.write('\nhi')
file.close()

# r: открывает файл в режиме «только для чтения». Этот режим применяется по умолчанию для функции open. Чтение файла начинается  с начала
# rb: открывает файл в режиме «только для чтения» в двоичном формате и начинает чтение с начала файла. Буква b обозначает слово binary(двоичный). Хотя двоичный формат можно использовать для разных целей, обычно он используется при работе с такими вещами, как изображения, видео и т. д.
# r+: открывает файл для чтения и записи, помещая указатель в начало файла.
# w: открывается в режиме «только для записи». Указатель помещается в начало файла, и это перезапишет любой существующий файл с таким же именем. Он создаст новый файл, если файл с таким именем не существует.
# wb: открывает файл в режиме «только для записи» в двоичном режиме.
# w+: открывает файл для записи и чтения.
# wb+: открывает файл для записи и чтения в двоичном режиме.
# a: открывает файл для добавления к нему новой информации. Указатель помещается в конец файла. Новый файл создается, если файл с таким именем не существует.
# ab: открывает файл для добавления в двоичном режиме.
# a+: открывает файл как для добавления, так и для чтения.
# ab+: открывает файл как для добавления, так и для чтения в двоичном режиме.