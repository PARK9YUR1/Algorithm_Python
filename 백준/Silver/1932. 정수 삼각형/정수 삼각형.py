N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * i for i in range(1, N+1)]

for i in range(N):
    for j in range(i+1):
        if i == 0:
            DP[i][j] = nums[i][j]
        else:
            if j == 0:
                DP[i][j] = DP[i-1][j] + nums[i][j]
            elif j == i:
                DP[i][j] = DP[i-1][j-1] + nums[i][j]
            else:
                DP[i][j] = max(DP[i-1][j-1] + nums[i][j], DP[i - 1][j] + nums[i][j])

result = max(DP[-1])
print(result)