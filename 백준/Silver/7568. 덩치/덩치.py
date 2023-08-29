N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

result = [[] for _ in range(N)]
for i in range(N):
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if P[i][0] < P[j][0] and P[i][1] < P[j][1]:
            cnt += 1
    result[i] = cnt

print(*result)