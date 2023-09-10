dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

def bfs(i, j):
    land = [(i, j)]

    while land:
        x, y = land.pop(0)
        box[x][y] = 0
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx in range(0, h) and ny in range(0, w) and box[nx][ny] == 1:
                box[nx][ny] = 0
                land.append((nx, ny))
    return 1

while True:
    w, h = map(int, input().split())  # 너비w, 높이h
    if w == h == 0:
        break
    box = [list(map(int, input().split())) for _ in range(h)]
    land, cnt = [], 0
    for i in range(h):
        for j in range(w):
            if box[i][j] == 1:
                cnt += bfs(i, j)
    print(cnt)