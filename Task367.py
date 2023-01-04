# Из строки hello получить h(e(l)l)o

def res(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + res(s[1:-1]) + ')' + s[-1]

text = input()
print(res(text))