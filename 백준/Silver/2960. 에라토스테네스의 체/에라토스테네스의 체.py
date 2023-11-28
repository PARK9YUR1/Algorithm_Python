N, K = map(int, input().split())
arr, x = [], 2
while len(arr) < K:
    for i in range(1, N//x+1):
        if len(arr) >= K:
            break
        num = x * i
        if num not in arr:
            arr.append(num)
    x += 1

print(arr[-1])
