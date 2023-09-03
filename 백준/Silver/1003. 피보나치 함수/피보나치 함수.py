DP = [0] * 42
DP[0] = 1
for i in range(2, 42):
    DP[i] = DP[i-1] + DP[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N], DP[N+1])