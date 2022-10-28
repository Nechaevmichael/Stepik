n = int(input())
for i in range(n):
    text = input()
    if len(text) > 10:
        print(f'{text[0]}{len(text) - 2}{text[-1]}')
    else:
        print(text)