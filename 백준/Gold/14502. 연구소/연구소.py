from itertools import combinations

def bfs(virus):
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    q = virus

    while q:
        x, y = q.pop(0)
        if arr[x][y] == 2:
            visited[x][y] = 2

        for dx, dy in [0, 1], [1, 0], [0, -1], [-1, 0]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == arr[nx][ny] == 0:
                visited[nx][ny] = 2
                cnt += 1
                q.append((nx, ny))
    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

empty, virus = [], []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

length = len(empty)
used = [0]*length

walls = list(combinations(empty, 3))
answer = []

for wall in walls:
    v = virus[:]
    for x, y in wall:
        arr[x][y] = 1
    ans = bfs(v)
    answer.append([ans, wall])
    for x, y in wall:
        arr[x][y] = 0

answer.sort()
result = length - answer[0][0] - 3
print(result)