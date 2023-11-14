X = {}
Y = {}

for _ in range(3):
    x, y = map(int, input().split())

    if x in X:
        X[x] += 1
    else:
        X[x] = 1

    if y in Y:
        Y[y] += 1
    else:
        Y[y] = 1


for x in X:
    if X[x] == 1:
        print(x, end=' ')
        break

for y in Y:
    if Y[y] == 1:
        print(y)
        break
