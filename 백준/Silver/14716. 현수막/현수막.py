# 14716
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
result = 0

def bfs(i, j):
    global visited, result
    q = [(i, j)]
    visited[i][j] = True
    result += 1

    while q:
        x, y = q.pop(0)
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == False and arr[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == False:
            bfs(i, j)

print(result)