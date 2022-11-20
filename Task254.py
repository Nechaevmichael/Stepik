# На вход программе подается натуральное число n (n<=1000). При помощи list comprehension создайте список, состоящий из делителей введенного числа.

# Sample Input 1:

# 4
# Sample Output 1:

# [1, 2, 4]

n = int(input())

list_comprehension = [i for i in range(1, n + 1) if n % i == 0]
print(list_comprehension)