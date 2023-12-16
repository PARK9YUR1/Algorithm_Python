# 11497
T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    arr = []
    idx = 0
    while L:
        x = L.pop()
        if idx % 2 == 0:
            arr.insert(0, x)
        else:
            arr.append(x)

        idx += 1

    mx = 0
    for i in range(1, N):
        x = abs(arr[i-1] - arr[i])
        mx = max(mx, x)
    print(mx)