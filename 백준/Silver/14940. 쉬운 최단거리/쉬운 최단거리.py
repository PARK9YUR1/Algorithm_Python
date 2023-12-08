# 14940
N, M = map(int, input().split())
# 0: 갈수없음 / 1: 갈수있음 / 2: 목표지점
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

sx = sy = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            sx, sy = i, j

def bfs(i, j):
    global visited
    q = [(i, j)]

    while q:
        x, y = q.pop(0)
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

bfs(sx, sy)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for vst in visited:
    print(*vst)