# Возвести число в степень с помощью рекурсии

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power(x, -n)
    if n % 2 == 0:
        return power(x, n//2) * power(x, n//2)
    else:
        return power(x, n - 1) * x
    
x = int(input())
n = int(input())
print(power(x, n))

def st(x, n):
    if n == 0:
        print(1)
    elif n == 1:
        print(x)
    else:
        result = 1
        for i in range(n):
            result *= x
        print(result)

st(3, 3)