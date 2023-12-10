# 16174
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

def dfs(x, y):
    visited[x][y] = True
    if visited[N-1][N-1] == True:
        return

    S = arr[x][y]

    for dx, dy in (0, S), (S, 0):
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
            dfs(nx, ny)

dfs(0, 0)
if visited[N-1][N-1] == True:
    print('HaruHaru')
else:
    print('Hing')