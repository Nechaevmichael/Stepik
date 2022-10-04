# На вход поступают два слова.

# Программа должна вывести True, если хотя бы одно слово равно слову "awesome".

# Сделать задачу необходимо без использования условного оператора.

# Sample Input 1:

# cool
# awesome
# Sample Output 1:

# True
word_1 = input()
word_2 = input()
print(word_1 == 'cool' or word_1 == 'awesome' or word_2 == 'cool' or word_2 == 'awesome')