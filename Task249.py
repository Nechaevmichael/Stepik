# Маленького, но очень смелого мышонка Брейна не взяли в летнюю школу юных злодеев. Он расстроился и решил отодвинуть свои планы по захвату мира, 
# а вместо этого податься в фотографы.
# Как вам наверняка известно, самые крутые фотографии получаются на пленку (ведь тогда в хештегах можно указать #пленка).
# Брейн наснимал очень много красочных фотографий на цветную и черно-белую пленки. Затем проявил и перевел их в цифровой вид. Но вот незадача! 
# Теперь цветные и черно-белые фотографии лежат в одной папке, и, чтобы их рассортировать, нужно потратить не один час!
# Так как Брейн теперь фотограф, а не программист, он просит вас помочь ему для одной фотографии определить, цветная она или черно-белая.
# Фотография представляет собой матрицу размера n × m, в каждой ячейке которой хранится символ, обозначающий цвет соответствующего пикселя. 
# Всего существует 6 цветов:
# 'C' (cyan) — голубой
# 'M' (magenta) — пурпурный
# 'Y' (yellow) — желтый
# 'W' (white) — белый
# 'G' (grey) — серый
# 'B' (black) — черный
# Фотографию можно считать черно-белой, если в ней есть только белый, серый или черный цвет. Если же присутствует хоть один пиксель голубого, 
# пурпурного или желтого цвета, она цветная.
# Входные данные
# В первой строке содержится два целых числа n и m (1 ≤ n, m ≤ 100) — количество строк и столбцов в матрице пикселей фотографии соответственно.
# Далее следуют n строк, описывающих строки матрицы. Каждая из них состоит из m разделенных пробелом символов, описывающих цвета пикселей в строке. 
# Каждый из символов в строке является одним из символов 'C', 'M', 'Y', 'W', 'G' или 'B'.
# Выходные данные
# В единственной строчке выведите «#Black&White» (без кавычек), если фотография черно-белая, и «#Color» (без кавычек), если цветная.
# Sample Input 1:
# 2 2
# C M
# Y Y
# Sample Output 1:
# #Color

n, m = map(int, input().split())
a = []
result = False
if n > 1:
    for i in range(n):
        a.append(list(map(str, input().split())))
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'B' or a[i][j] == 'G' or a[i][j] == 'W':
                result = False
            else:
                result = True
if n == 1:
    a.append(list(map(str, input().split())))
    for i in range(1):
        if a[i] == 'B' or a[i] == 'G' or a[i] == 'W':
            result = False
        elif a[i] == 'C':
            result = True
if result == False:
    print('#Black&White')
else:
    print('#Color')