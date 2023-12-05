# 2583
M, N, K = map(int, input().split())  # M x N, 직사각형 K개
arr = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

def bfs(i, j):
    global visited
    q = [(i, j)]
    visited[i][j] = True
    cnt = 1

    while q:
        x, y = q.pop(0)
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == False and arr[nx][ny] == 0:
                cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = True

    return cnt

result = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and visited[i][j] == False:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result)