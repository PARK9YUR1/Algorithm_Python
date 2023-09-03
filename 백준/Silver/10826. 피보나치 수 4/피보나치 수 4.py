DP = [0] * 10001
DP[0], DP[1] = 0, 1

N = int(input())
for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2]
print(DP[N])