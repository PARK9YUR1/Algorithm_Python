from collections import deque

def bfs(i, j, used):
    q = deque()
    q.append([i, j, used])

    while q:
        u, x, y = q.popleft()
        if (x, y) == (N-1, M-1):
            return visited[u][x][y]

        for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 다음=0(이동가능), visited=0(방문 x)
                if arr[nx][ny] == 0 and visited[u][nx][ny] == 0:
                    visited[u][nx][ny] = visited[u][x][y] + 1
                    q.append([u, nx, ny])
                # 다음=1(벽), u=0(아직 벽 안 부숨)
                elif arr[nx][ny] == 1 and u == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    q.append([1, nx, ny])

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[[0]*M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = 1

result = bfs(0, 0, 0)
if result:
    print(result)
else:
    print(-1)