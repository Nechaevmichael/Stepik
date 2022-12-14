# Недавно у Антона появилось множество, состоящее из маленьких латинских букв. Он аккуратно выписал все буквы, которые в него входят 
# в одну строку через запятую. Для красоты он так же добавил в начало этой строки открывающуюся фигурную скобку, а в конец — закрывающуюся.
# К сожалению, Антон иногда забывал, что уже записал некоторую букву, и выписывал ее снова. 
# Он просит вас посчитать общее число различных букв в его множестве.
# Входные данные
# В первой и единственной строке задано описание множества букв. Длина строки не превышает 1000. 
# Гарантируется, что строка начинается с открывающейся фигурной скобки, а заканчивается закрывающейся. 
# Между ними через запятую перечислены маленькие латинские буквы. После каждой запятой следует пробел.
# Выходные данные
# Выведите единственное число — количество различных букв в множестве Антона.
# Sample Input 1:
# {a, b, c}
# Sample Output 1:
# 3
text = input()
text_1 = [i for i in text if i.isalpha()]
print(len(set(text_1)))