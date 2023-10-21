N = int(input())
arr = list(map(int, input().split()))
arr.sort(key=lambda x:abs(x))

s, e = 0, 1
mn_abs = 10 ** 10
result = []
while True:
    if e == N:
        break
    ans = arr[s] + arr[e]
    if mn_abs > abs(ans):
        mn_abs = abs(ans)
        result = [arr[s], arr[e]]
    s, e = s+1, e+1

result.sort()
print(*result)