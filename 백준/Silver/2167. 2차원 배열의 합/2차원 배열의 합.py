import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for _ in range(K):
    result = 0
    i, j, x, y = map(int, input().split())
    for a in range(i-1, x):
        result += (sum(box[a][j-1:y]))
    print(result)