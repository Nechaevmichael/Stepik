import json
from pprint import pprint
from random import randint
str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
"""
data = json.loads(str_json)
# pprint(type(data))
# pprint(data['response']['count'])
# pprint(data['response']['items'])

# ==============================
# Обойдем циклом строку json
# for item in data['response']['items']:
#     print(item['first_name'], item['last_name'])

# ==============================
# Удалим элемент id и добавим likes
for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(0, 1000)

# pprint(data['response']['items'])

# ===============================
# Сконвертируем обратно словарь в строку json
new_json = json.dumps(data)
pprint(new_json)
print('Ниже json с параметром indent'.center(40, '-'))
json_indent = json.dumps(data, indent=2)
print(json_indent)