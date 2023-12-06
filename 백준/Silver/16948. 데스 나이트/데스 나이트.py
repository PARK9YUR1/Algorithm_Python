# 16948
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0]*N for _ in range(N)]

def bfs(i, j):
    global visited
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        x, y = q.pop(0)
        if x == r2 and y == c2:
            return visited[x][y] - 1
        for dx, dy in (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

result = bfs(r1, c1)
if result == None:
    result = -1
print(result)