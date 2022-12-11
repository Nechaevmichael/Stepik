# Перед вами словарь user
# Напишите программу для создания нового словаря, которая извлекает указанные ключи из приведенного ниже словаря.
# Сами значения ключей, которые нужно извлечь, поступает на вход программе в виде одной строки разделенные пробелом
# В качестве ответа выведите на экран полученный словарь
# Sample Input 1:
# last_name gender
# Sample Output 1:
# {'last_name': 'Wehner', 'gender': 'Non-binary'}

user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {
        "title": "Central Hospitality Liaison",
        "key_skill": "Organisation"
    },
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual"
    }
}
keys = list(map(str, input().split()))
# result = {}
# for i in keys:
#     if i in user:
#         result[i] = user[i]
# print(result)

res = {i: user[i] for i in keys if i in user}
print(res)