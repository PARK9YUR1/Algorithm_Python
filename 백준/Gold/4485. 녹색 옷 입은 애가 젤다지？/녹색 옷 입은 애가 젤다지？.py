import heapq
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra():
    arr[0][0] = box[0][0]
    min_heap = [(arr[0][0], 0, 0)]

    while min_heap:
        cur_rupee, x, y = heapq.heappop(min_heap)
        if cur_rupee > arr[x][y]:
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                new_rupee = cur_rupee + box[nx][ny]
                if arr[nx][ny] > new_rupee:
                    arr[nx][ny] = new_rupee
                    heapq.heappush(min_heap, (new_rupee, nx, ny))

tc = 0
while True:
    tc += 1
    N = int(input())  # 동굴의 크기
    if N == 0:
        break
    box = [list(map(int, input().split())) for _ in range(N)]
    arr = [[10 * N**2]*N for _ in range(N)]
    dijkstra()
    print(f'Problem {tc}: {arr[N-1][N-1]}')