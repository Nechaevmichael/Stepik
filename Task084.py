# Программа запрашивает у пользователя курс доллара - вещественное число,  и также 
# количество долларов(целое число), которое пользователь хочет приобрести. 
# В итоге программа должна вывести следующее сообщение:
# "Current dollar rate is <курс доллара>. You want buy <количество долларов> dollars
# You must pay <стоимость>"
# Sample Input:
# 56.77
# 11
# Sample Output:
# Current dollar rate is 56.77. You want buy 11 dollars
# You must pay 624.47

course_dollar = float(input('Введите курс доллара: '))
count_dollar = int(input('Введите количество валюты к приобретению: '))
print(f'''Current dollar rate is {count_dollar}. You want buy {count_dollar} dollars
You must pay {count_dollar * course_dollar}''')