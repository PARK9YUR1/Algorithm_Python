n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
DP = [[0]*m for _ in range(n)]
mx = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
        mx = max(mx, DP[i][j])

print(mx**2)