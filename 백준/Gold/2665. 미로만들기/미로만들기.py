import heapq

def bfs():
    global cnt
    q = [(0, 0, 0)]
    dist = [[0] * N for _ in range(N)]
    dist[0][0] = 1

    while q:
        d, x, y = heapq.heappop(q)
        if x == y == N-1:
            print(d-1)
            break
        for dx, dy in [0, 1], [-1, 0], [0, -1], [1, 0]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == 0:
                if arr[nx][ny] == 1:  # 흰
                    dist[nx][ny] = dist[x][y]
                    heapq.heappush(q, (dist[nx][ny], nx, ny))
                else:  # 검
                    dist[nx][ny] = dist[x][y] + 1
                    heapq.heappush(q, (dist[nx][ny], nx, ny))


N = int(input())  # 한줄에 들어가는 방의 수
arr = [list(map(int, input())) for _ in range(N)]  # 0:검은방, 1:흰방
bfs()