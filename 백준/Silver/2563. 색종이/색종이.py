N = int(input())

box = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            box[i][j] += 1

result = 0
for i in range(100):
    for j in range(100):
        if box[i][j] > 0:
            result += 1

print(result)