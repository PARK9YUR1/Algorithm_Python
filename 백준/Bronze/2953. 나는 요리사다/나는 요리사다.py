score = [list(map(int, input().split())) for _ in range(5)]
res = []
mx = 0
for i in range(5):
    ans = 0
    for j in range(4):
        ans += score[i][j]
    res.append((i+1, ans))
res.sort(key=lambda x:-x[1])
print(*res[0])