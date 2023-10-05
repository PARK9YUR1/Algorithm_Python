import sys
input = sys.stdin.readline

N = int(input())  # 지방의 수
arr = list(map(int, input().split()))  # 각 지방의 예산요청
M = int(input())  # 총 예산
arr.sort()

start, end = 0, arr[-1]

while start <= end:
    mid = (start+end) // 2
    total = 0

    for a in arr:
        if a >= mid:
            total += mid
        else:
            total += a

    if total <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)