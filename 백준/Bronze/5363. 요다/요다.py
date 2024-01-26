N = int(input())
for _ in range(N):
    arr = list(input().split())
    arr = arr[2:] + arr[:2]
    print(' '.join(arr))