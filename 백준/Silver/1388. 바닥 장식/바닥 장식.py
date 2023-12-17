# 1388
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def bfs(i, j):
    global visited, result
    q = [(i, j)]
    visited[i][j] = True
    result += 1

    while q:
        x, y = q.pop(0)
        if arr[x][y] == '-':
            for dx, dy in (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == '-':
                    q.append((nx, ny))
                    visited[nx][ny] = True
        else:
            for dx, dy in (1, 0), (-1, 0):
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == '|':
                    q.append((nx, ny))
                    visited[nx][ny] = True


result = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            bfs(i, j)

print(result)