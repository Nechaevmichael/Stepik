# В переменную starts_with присвойте lambda функцию, которая принимает строку и возвращает True, 
# когда переданная строка начинается с буквы W. Во всех остальных случаях нужно возвращать False

# Ничего кроме создания переменной starts_with делать не нужно

starts_with = lambda x: True if x[0] == 'W' else False

print(starts_with('World'))