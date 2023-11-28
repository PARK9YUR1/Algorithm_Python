# 11123
def bfs(i, j):
    global visited, cnt

    q = [(i, j)]
    visited[i][j] = True
    cnt += 1

    while q:
        x, y = q.pop(0)
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W:
                if arr[nx][ny] == '#' and visited[nx][ny] != True:
                    q.append((nx, ny))
                    visited[nx][ny] = True


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())  # 높이, 너비
    arr = [list(input()) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and visited[i][j] != True:
                bfs(i, j)

    print(cnt)