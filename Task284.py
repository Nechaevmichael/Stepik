# Переменные countries соединяют ряд стран с тремя крупнейшими городами каждой страны. 

# Программе на вход будет поступать название города в переменную city. И ваша задача найти какой стране 
# принадлежит введенный город. Если страна успешно найдена, необходимо вывести сообщение:

# INFO: <City> is a city in <Country>
# в противном случае

# ERROR: Country for {City} not found
# Учитывайте, что регистр букв имеет значение

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
city = city.capitalize()
country = ''
result = False

for key, value in countries.items():
    if city in value:
        country = key
        result = True
        break
if result:
    print(f'INFO: {city} is a city in {country}')
else:
    print(f'ERROR: Country for {city} not found')