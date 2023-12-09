# 1189
R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
visited[R-1][0] = 1
result = 0

def dfs(x, y):
    global result
    if x == 0 and y == C-1:
        if visited[x][y] == K:
            result += 1
        return

    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != 'T' and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny)
            visited[nx][ny] = 0

dfs(R-1, 0)
print(result)