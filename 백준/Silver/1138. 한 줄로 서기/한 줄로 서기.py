N = int(input())
arr = list(map(int, input().split()))[::-1]
result = []

for i in range(N):
    idx = arr[i]
    result.insert(idx, N-i)

print(*result)