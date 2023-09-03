def dfs(x, y):
    global cnt, box
    cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and box[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)

N = int(input())
box = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
result = []

for i in range(N):
    for j in range(N):
        if box[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)