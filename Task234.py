# На вход программе поступает строка, состоящая из нескольких слов, знаком разделителем между словами 
# будем считать символ пробела. Ваша задача исключить из строки дублирующие слова: первое появление 
# слова остается в строке, второе и все последующие появления исключаются. 
# При сравнении на дубли строк регистр букв не учитывать, это значит слова python и PyThOn считаются одинаковыми.
# В качестве ответа необходимо вывести итоговую строку без дублей.
# Sample Input 1:
# Python is best I love python
# Sample Output 1:
# Python is best I love

origin = list(map(str, input().split()))
temp = []
result = []

for i in range(len(origin)):
    if origin[i].lower() not in temp:
        temp.append(origin[i].lower())
        result.append(origin[i])
print(*result)
