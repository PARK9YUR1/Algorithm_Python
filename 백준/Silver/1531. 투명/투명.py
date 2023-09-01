pic = [[0] * 100 for _ in range(100)]
N, M = map(int, input().split())
for _ in range(N):
    x, y, i, j = map(int, input().split())
    for a in range(x-1, i):
        for b in range(y-1, j):
            pic[a][b] += 1
result = 0
for i in range(100):
    for j in range(100):
        if pic[i][j] > M:
            result += 1
print(result)