# При игре в "Города" игроки по очереди называют названия городов так, чтобы первая буква каждого нового
# слова совпадала с последней буквой предыдущего. При этом считают, что если последняя буква предыдущего слова — 
# мягкий знак, то с первой буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.
# Напишите программу, которая считывает подряд две строки, после чего выводит «Good», если последний 
# символ первой строки совпадает с первым символом второй (с учётом правила про мягкий знак), и «Bad» в противном случае.
# Sample Input 1:
# Лондон
# Норильск
# Sample Output 1:
# Good

city_1 = input().lower()
city_2 = input().lower()

if city_1[-1] == city_2[0]:
    print('Good')
else:
    if city_1[-1] == 'ь':
        if city_1[-2] == city_2[0]:
            print('Good')
        else:
            print('Bad')
    else:
        print('Bad')
