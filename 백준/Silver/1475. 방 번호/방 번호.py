N = input()

num = [0] * 10
for i in range(10):
    num[i] = N.count(str(i))

six = N.count('6')
nine = N.count('9')
if six < nine:
    num[9] -= (nine - six)//2
elif six > nine:
    num[6] -= (six - nine)//2

mx = max(num)
print(mx)