N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start, end = 0, 1
mn = arr[-1] - arr[0]

while True:
    if end == N or start == N:
        break
    x = arr[end] - arr[start]
    if x < M:
        end += 1
    else:
        mn = min(mn, x)
        start += 1

print(mn)