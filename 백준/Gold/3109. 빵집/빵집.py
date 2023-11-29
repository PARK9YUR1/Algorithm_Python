# 3109

def dfs(x, y):
    global visited, cnt, check

    if check == True:
        return

    visited[x][y] = True

    for dx, dy in (-1, 1), (0, 1), (1, 1):
        nx, ny = x+dx, y+dy

        if check == True:
            break

        if 0 <= nx < R and 0 < ny < C and arr[nx][ny] != 'x' and visited[nx][ny] != True:
            visited[nx][ny] = True
            if ny == C-1:
                check = True
            else:
                dfs(nx, ny)

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
cnt = 0

for i in range(R):
    check = False
    dfs(i, 0)
    if check == True:
        cnt += 1

print(cnt)