# Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит 
# сообщение о том, являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются 
# английскими строчными буквами.
# Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется, 
# что значение колонок это латинские буквы abcdefgh, а строки это символы цифр от 1-8
# Разбор Youtube Patreon Boosty
# Sample Input 1:
# a1
# b2
# Sample Output 1:
# YES

a = input()
b = input()

black = ['a1', 'a3', 'a5', 'a7', 'b2', 'b4', 'b6', 'b8', 'c1', 'c3', 'c5', 'c7', 'd2', 'd4', 'd6', 'd8', 'e1',
'e3', 'e5', 'e7', 'f2', 'f4', 'f6', 'f8', 'g1', 'g3', 'g5', 'g7', 'h2', 'h4', 'h6', 'h8']

white = ['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8', 'd1', 'd3', 'd5', 'd7', 'e2',
'e4', 'e6', 'e8', 'f1', 'f3', 'f5', 'f7', 'g2', 'g4', 'g6', 'g8', 'h1', 'h3', 'h5', 'h7']
if a in black and b in black or a in white and b in white:
    print('YES')
else:
    print('NO')