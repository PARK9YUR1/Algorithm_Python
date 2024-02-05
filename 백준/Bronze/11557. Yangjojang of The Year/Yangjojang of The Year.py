T = int(input())
for _ in range(T):
    N = int(input())
    arr = [tuple(input().split()) for _ in range(N)]
    arr.sort(key=lambda x:-int(x[1]))
    print(arr[0][0])