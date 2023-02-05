# Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит 
# самое длинное слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной, 
# нужно вернуть слово, которое встречается последнее в тексте.
# При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.  
# И также учитывайте, что слова в тестах будут как на русском языке, так и на английском.
# Если бы содержимое файла было таким:
# He was running, but it was like running through deep water. There were trees all around him, 
# trees which tried to stop him. They reached out with their branches. 
# And it was behind him. It was coming nearer. 
# то ответом было бы слово branches
# Все возможные знаки пунктуации можно получить из модуля string
# from string import punctuation

def longest_word_in_file(file_name: str) -> None:
    open_file = open(file_name, 'r', encoding='utf-8')
    from string import punctuation
    max_word = ''
    for line in open_file:
        words = line.split()
        for word in words:
            for i in word:
                if i in punctuation:
                    word = word.replace(i, '')
                else:
                    continue
            if len(word) >= len(max_word):
                max_word = word
    return max_word
        
print(longest_word_in_file('text_1.txt'))