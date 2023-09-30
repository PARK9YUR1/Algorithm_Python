import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def f(r, c):
    global DP
    if c == 0:
        DP[r][c] = arr[r][c]
        return DP[r][c]
    else:
        DP[r][c] = f(r, c-1) + arr[r][c]
        return DP[r][c]

N, M = map(int, input().split())  # N:표의크기 / M:합 구하는 횟수
arr = [list(map(int, input().split())) for _ in range(N)]

DP = [[0]*N for _ in range(N)]
for i in range(N):
    f(i, N-1)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x, y = x1-1, y1-1
    result = 0
    for i in range(x, x2):
        if y == 0:
            result += DP[i][y2-1]
        else:
            result += (DP[i][y2-1] - DP[i][y-1])
    print(result)
