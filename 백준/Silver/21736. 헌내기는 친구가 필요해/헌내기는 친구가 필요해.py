def bfs(i, j):
    global visited
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx in range(0, N) and ny in range(0, M) and box[nx][ny] in ['O', 'P'] and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

N, M = map(int, input().split())
# O:빈공간 / X:벽 / I:도연 / P:사람
box = [list(map(str, input())) for _ in range(N)]
p = []  # 사람들 위치
for i in range(N):
    for j in range(M):
        if box[i][j] == 'I':
            si, sj = i, j
        elif box[i][j] == 'P':
            p.append((i, j))

visited = [[0]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

bfs(si, sj)

result = 0
for pi, pj in p:
    if visited[pi][pj] != 0:
        result += 1
if result == 0:
    result = 'TT'
print(result)