# N:현재휴게소 개수 / M:더 지으려는 휴게소 개수 / L:고속도로 길이
N, M, L = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [L] # 휴게소 위치
arr.sort()

start, end = 1, L
while start < end:
    mid = (start + end) // 2
    cur, cnt = arr[0], 0
    for i in range(1, N+2):
        dist = arr[i] - cur
        if dist > mid:
            cnt += (dist - 1)//mid
        cur = arr[i]

    if cnt > M:
        start = mid + 1
    else:
        end = mid
print(start)
