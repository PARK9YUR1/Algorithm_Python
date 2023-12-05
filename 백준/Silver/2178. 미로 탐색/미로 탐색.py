# 2178
N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def bfs(i, j):
    global visited
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        x, y = q.pop(0)
        if x == N-1 and y == M-1:
            return visited[x][y]
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == '1' and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

result = bfs(0, 0)
print(result)