# 5800
K = int(input())
for tc in range(1, K+1):
    arr_ = list(map(int, input().split()))
    N, arr = arr_[0], arr_[1:]
    arr.sort(reverse=True)
    mx, mn = max(arr), min(arr)
    gap = 0
    for i in range(1, N):
        x = arr[i-1] - arr[i]
        gap = max(gap, x)

    print(f'Class {tc}')
    print(f'Max {mx}, Min {mn}, Largest gap {gap}')