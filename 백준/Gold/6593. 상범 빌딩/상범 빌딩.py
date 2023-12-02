while True:
    # L:상범빌딩 층수 / R, C: 상범빌딩 한층의 행과 열의 개수
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    building = []
    start = []

    for i in range(L):
        arr = []
        for j in range(R):
            arr2 = list(input())
            if 'S' in arr2:
                for k in range(C):
                    if arr2[k] == 'S':
                       start.append((i, j, k))
            arr.append(arr2)
        building.append(arr)
        x = input()

    dz = [0, 0, 0, 0, -1, 1]  # 층
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]

    q = start
    sz, sx, sy = q[0]
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    visited[sz][sx][sy] = 1

    time = 0

    while q:
        if time > 0:
            break
        z, x, y = q.pop(0)
        for k in range(6):
            nz, nx, ny = z+dz[k], x+dx[k], y+dy[k]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and visited[nz][nx][ny] == 0 and building[nz][nx][ny] != '#':
                q.append((nz, nx, ny))
                visited[nz][nx][ny] = visited[z][x][y] + 1
                if building[nz][nx][ny] == 'E':
                    time = visited[z][x][y]

    if time > 0:
        print(f'Escaped in {time} minute(s).')
    else:
        print('Trapped!')