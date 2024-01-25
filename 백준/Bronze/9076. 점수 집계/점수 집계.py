T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    total = sum(arr[1:4])
    tmp = arr[3] - arr[1]
    if tmp >= 4:
        print('KIN')
    else:
        print(total)