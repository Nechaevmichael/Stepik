# Перед вами два словаря d1 и d2

# Ваша задача выполнить слияние этих словарей в переменную capitals и затем вывести ее на экран

d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}

d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}

capitals = d1 | d2
print(capitals)