L, P = map(int, input().split())
arr = list(map(int, input().split()))
N = L * P

for a in arr:
    print(a-N, end=' ')