S = str(input())

for i in range(97, 123):
    alpha = chr(i)
    print(S.find(alpha), end = ' ')