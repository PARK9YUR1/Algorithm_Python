N = int(input())  # 두 전봇대 사이의 전깃줄
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])
lst = []
for i in range(N):
    lst.append(arr[i][1])


DP = [1]*N
for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i]:
            DP[i] = max(DP[i], DP[j]+1)
            # DP[i] = DP[j]+1
mx = max(DP)


arr.sort(key=lambda x:x[1])
lst = []
for i in range(N):
    lst.append(arr[i][0])
DP = [1]*N
for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i]:
            DP[i] = max(DP[i], DP[j]+1)
            # DP[i] = DP[j]+1
mx = max(max(DP), mx)

print(N-mx)
