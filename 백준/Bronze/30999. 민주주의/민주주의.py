N, M = map(int, input().split())
result = 0
for _ in range(N):
    res = list(input())
    if res.count('O') > M//2:
        result += 1
print(result)