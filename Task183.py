# На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее 
# положительное значение. В случае, если положительных значений нет, выведите строку "Empty"

# Sample Input 1:

# 8 11 -9 0 5 -20
# Sample Output 1:

# 5

numbers = list(map(int, input().split()))
# min = numbers[0]
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         if min > numbers[i]:
#             min = numbers[i]
# if min > 0:
#     print(min)
# else:
#     print('Empty')
L = []
for i in range(len(numbers)):
    if numbers[i] > 0:
        L.append(numbers[i])

if L == []:
    print('Empty')
else:
    min = L[0]
    for i in range(len(L)):
        if min > L[i]:
            min = L[i]
    print(min)
