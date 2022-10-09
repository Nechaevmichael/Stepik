# Напишите программу, которая сначала считывает две фразы по очереди, а потом воспроизводит 
# их в той же последовательности, каждую на отдельной строчке.

# Sample Input 1:

# Hello!
# Hi!
# Sample Output 1:

# Hello!
# Hi!

phrase_1 = input()
phrase_2 = input()
print(phrase_1, phrase_2, sep='\n')