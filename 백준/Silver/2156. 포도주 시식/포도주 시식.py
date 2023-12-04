# 2156
N = int(input())
DP = [0]*N
arr = [int(input()) for _ in range(N)]

if N >= 3:
    for i in range(N):
        if i == 0:
            DP[i] = arr[i]
        elif i == 1:
            DP[i] = arr[i] + DP[i-1]
        elif i == 2:
            DP[i] = max(arr[i-2] + arr[i], arr[i-1] + arr[i], DP[i-1])
        else:
            DP[i] = max(DP[i-1], DP[i-2] + arr[i], DP[i-3] + arr[i-1] + arr[i])
    print(max(DP))
else:
    print(sum(arr))

