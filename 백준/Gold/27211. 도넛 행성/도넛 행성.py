# 27211
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 0:빈칸 / 1:숲(막힘)
visited = [[False]*M for _ in range(N)]

def bfs(i, j):
    global visited
    q = [(i, j)]
    visited[i][j] = True

    while q:
        x, y = q.pop(0)
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = (x+dx)%N, (y+dy)%M
            if arr[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visited[i][j]:
            result += 1
            bfs(i, j)

print(result)