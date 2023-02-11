# В вашем распоряжении имеется следующий файл. Ваша задача скачать его и найти сколько уникальных слов 
# используется в этом тексте, при этом регистр букв не нужно учитывать. Это значит, что слова Lorem и loRem 
# являются эквивалентными.
# Например, если перед вами был бы такой текст:
# Привет как дела
# привет хорошо
# то здесь четыре уникальных слова.
# Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.
# В качестве ответа укажите количество уникальных слов

def unique_words(file_name: str) -> int:
    l = []
    with open(file_name, 'r', encoding='utf') as file:
        for i in file:
            l.append(i.split())
    result = []
    for i in l:
        for j in i:
            if j.lower() not in result:
                result.append(j.lower())
    count_unique = len(result)
    return count_unique       

print(unique_words('lorem.txt'))
    