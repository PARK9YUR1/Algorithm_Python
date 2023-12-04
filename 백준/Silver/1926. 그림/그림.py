# 1926
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(i, j):
    global visited, pic
    q = [(i, j)]
    visited[i][j] = True

    while q:
        x, y = q.pop(0)
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and arr[nx][ny] == 1:
                visited[nx][ny] = True
                pic += 1
                q.append((nx, ny))

cnt = 0
mx = 0
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == False:
            pic = 1
            cnt += 1
            bfs(i, j)
            mx = max(mx, pic)

print(cnt)
print(mx)
