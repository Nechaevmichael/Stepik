# После вечеринки компания из N человек хочет добраться домой с помощью такси. 
# Максимальное количество человек, которое может уместиться в машину равно 4. 
# Сколько машин придется вызвать ребятам, чтобы все могли уехать?

# Программа получает на вход положительное целое число N - количество человек в компании.

# Sample Input 1:

# 16
# Sample Output 1:

# 4
import math
people = int(input())
count_taxi = math.ceil(people / 4)
print(count_taxi)