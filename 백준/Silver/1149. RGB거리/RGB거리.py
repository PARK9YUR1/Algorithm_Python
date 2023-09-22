import sys
input = sys.stdin.readline

N = int(input())  # 집의 수
costs = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * 3 for _ in range(N)]
for color in range(3):
    DP[0][color] = costs[0][color]

for i in range(1, N):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + costs[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + costs[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + costs[i][2]

mn = min(DP[i][0], DP[i][1], DP[i][2])

print(mn)