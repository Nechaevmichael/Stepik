# На вход программе поступает слово. Вам необходимо воспроизвести процесс, в котором каждый раз
# у этого слово будет пропадать первая и последняя буква. Этот процесс необходимо закончить, 
# когда в слове останется только одна буква или слово  станет пустой строкой. 
# При этом результат каждого этапа нужно выводить
# Sample Input 1:
# Правильность
# Sample Output 1:
# Правильность
# равильност
# авильнос
# вильно
# ильн
# ль

text = input()
while len(text) != 0:
    text = text[1:]
    text = text[:-1]
    print(text)