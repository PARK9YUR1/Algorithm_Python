# 3184
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

def bfs(i, j):
    global visited
    q = [(i, j)]
    visited[i][j] = True
    sheep = wolf = 0
    if arr[i][j] == 'o':
        sheep += 1
    else:
        wolf += 1

    while q:
        x, y = q.pop(0)
        for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != '#' and visited[nx][ny] == False:
                if arr[nx][ny] == 'o':
                    sheep += 1
                elif arr[nx][ny] == 'v':
                    wolf += 1
                q.append((nx, ny))
                visited[nx][ny] = True

    return [sheep, wolf]

S = W = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] in 'vo' and visited[i][j] == False:
            s, w = bfs(i, j)
            if s > w:
                S += s
            else:
                W += w

print(S, W)
