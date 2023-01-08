# Представьте, у нас есть список товаров и их стоимость, но мы хотим взглянуть на него в отсортированном виде. 
# Вверху хотим видеть самые дорогие товары, внизу самые дешевые
# Программа будет принимать строки, в которых сперва указывается название товара, а затем через двоеточие с пробелом его цена - целое положительное число.
# Строка "конец" означает списка товаров и соответственно окончание ввода
# Все товары имеют уникальные названия, цены не дублируются.
# Ваша задача вывести список товаров по уменьшению цены
# Sample Input:
# Sony PlayStation 5: 46000
# Телевизор QLED Samsung QE65Q60TAU: 87090
# Смартфон Samsung Galaxy A11: 10000
# Планшет Samsung Galaxy Tab S6: 26600
# конец
# Sample Output:
# Телевизор QLED Samsung QE65Q60TAU
# Sony PlayStation 5
# Планшет Samsung Galaxy Tab S6
# Смартфон Samsung Galaxy A11

# product = []
# while True:
#     item = input()
#     if item != 'конец':
#         product.append(item)
#     else:
#         break

# product = sorted(product, key=lambda x: int(x.split(':')[1]), reverse=True)
# product_1 = []
# for i in product:
#     i = i.split(':')
#     product_1.append(i)
# for i in product_1:
#     print(i[0])

products = {}
while True:
    item = input()
    if item != "конец":
        temp = item.split(': ')
        products[temp[0]] = temp[1]
    else:
        break

for i in sorted(products.items(), key=lambda para: para[1], reverse=True):
    print(i[0])