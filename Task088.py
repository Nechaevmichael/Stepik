# Вводится целое число, необходимо вывести его на экран, отведя как минимум 10 разрядов под
# отображение числа. Если в числе не хватает разрядов, необходимо выводить незначащие нули

# Sample Input 1:

# 57
# Sample Output 1:

# 0000000057

number = int(input())
print(f'{number:010d}')
print(f'{number:10d}')
print(f'{number:_d}')
sep = ','
print(f'{number:{sep}d}')