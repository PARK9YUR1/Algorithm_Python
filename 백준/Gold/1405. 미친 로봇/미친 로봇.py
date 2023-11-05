arr = list(map(int, input().split()))
N, dir = arr[0], [arr[i]/100 for i in range(1, 5)]
visited = [[False]*29 for _ in range(29)]
ans = 0

#     동 서  남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, depth, pstack):
    global ans
    visited[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if visited[nx][ny] == False:
            if depth == N:  # N번 이동한 경우
                ans += pstack * dir[k]  # 확률을 더함
            else:
                dfs(nx, ny, depth+1, pstack * dir[k])
    visited[x][y] = False

dfs(14, 14, 1, 1)  # 시작점 : 중앙
print(ans)