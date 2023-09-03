N, K = map(int, input().split())
DP = [[0]*(K+1) for _ in range(N+1)]
DP[1][1] = 1
for i in range(2, N+1):
    for j in range(1, K+1):
        if j == 1 or i == j:
            DP[i][j] = 1
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j]
print(DP[N][K])