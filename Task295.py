# В вашем распоряжении есть двумерный список vector. Ваша задача при помощи генератора-списка сделать на основании vector 
# линейный(одномерный ) список и вывести его

vector = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9], 
          [10, 11, 12], 
          [13, 14, 15], 
          [16, 17, 18]]

# result = []
# for i in vector:
#     for j in range(len(i)):
#         result.append(i[j])
# print(result)

result = [i[j] for i in vector for j in range(len(i))]
print(result)