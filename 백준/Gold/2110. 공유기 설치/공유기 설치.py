import sys
input = sys.stdin.readline

N, C = map(int, input().split())  # N:집 개수 / C:공유기 개수
x = [int(input()) for _ in range(N)]  # 집 좌표
x.sort()

start, end = 1, x[-1]-x[0]

while start <= end:
    mid = (start + end) // 2
    idx, cnt = 0, 1
    for i in range(1, N):
        if x[i] - x[idx] >= mid:
            cnt += 1
            idx = i

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)