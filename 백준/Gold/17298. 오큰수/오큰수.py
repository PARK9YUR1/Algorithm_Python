import sys
input = sys.stdin.readline

N = int(input())
result = [-1]*N
A, idx = [], 0
for n in input().split():
    n = int(n)
    if len(A) != 0:
        while True:
            if len(A) == 0 or A[-1][1] >= n:
                break
            if A[-1][1] < n:
                i, ans = A.pop()
                result[i] = n
    A.append((idx, n))
    idx += 1
print(*result)