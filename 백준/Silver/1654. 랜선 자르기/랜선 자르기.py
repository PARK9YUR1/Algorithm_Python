import sys
input = sys.stdin.readline

K, N = map(int, input().split())  # K:이미 가지고 있는 랜선 개수 / N:필요한 랜선 개수
arr = [int(input()) for _ in range(K)]  # 가지고 있는 랜선 길이

start, end = 1, sum(arr)//N

while start <= end:
    mid = (start+end) // 2
    ans = 0

    for a in arr:
        ans += a//mid

    if ans >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
