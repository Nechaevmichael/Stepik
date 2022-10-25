# Найти НОД

a, b = map(int, input().split())

while b > 0:
    a, b = b, a % b
print(a)

# Найти НОД методом вычитания

a, b = map(int, input().split())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)