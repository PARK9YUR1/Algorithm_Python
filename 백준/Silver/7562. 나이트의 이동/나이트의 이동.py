# 7562
T = int(input())
for _ in range(T):
    L = int(input())  # 체스판 한변 길이
    cx, cy = map(int, input().split())  # 나이트 현재 칸
    mx, my = map(int, input().split())  # 나이트가 이동하려고 하는 칸
    visited = [[0] * L for _ in range(L)]

    def bfs(i, j):
        global visited
        q = [(i, j)]
        visited[i][j] = 1

        while q:
            x, y = q.pop(0)
            if x == mx and y == my:
                return visited[x][y] - 1
            for dx, dy in (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2):
                nx, ny = x+dx, y+dy
                if 0 <= nx < L and 0 <= ny < L and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    result = bfs(cx, cy)
    print(result)
