
n = int(input())
winner_Mishka = 0
winner_Chris = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        winner_Mishka += 1
    else:
        if a < b:
            winner_Chris += 1
        else:
            winner_Chris += 1
            winner_Mishka += 1
if winner_Chris > winner_Mishka:
    print("Chris")
else:
    if winner_Chris < winner_Mishka:
        print('Mishka')
    else:
        print('Friendship is magic!^^')