# На вход программе поступает строка, ваша задача удалить из нее все символы "w" и "z".

# Учитываем только маленькие буквы

# Sample Input:

# what's up?
# Sample Output:

# hat's up?

text = input().lower()
result_1 = text.replace('w', '')
result_2 = result_1.replace('z', '')
print(result_2)