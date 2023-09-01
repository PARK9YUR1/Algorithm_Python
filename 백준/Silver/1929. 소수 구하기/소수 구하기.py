import sys
input = sys.stdin.readline

M, N = map(int, input().split())
nums = [x for x in range(M, N+1)]
n = int(N ** 0.5)
checked = [True] * (N+1)

for i in range(2, n+1):
    for j in range(i, N+1, i):
        if i == j:
            continue
        checked[j] = False

for i in range(M, N+1):
    if i != 1 and checked[i] == True:
        print(i)