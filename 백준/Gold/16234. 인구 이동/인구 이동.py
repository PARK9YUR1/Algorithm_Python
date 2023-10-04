def bfs(x, y):
    global visited
    cnt = 0
    lst = []
    total = 0
    queue = [(x, y)]

    while queue:
        i, j = queue.pop(0)
        for di, dj in [0, 1], [1, 0], [-1, 0], [0, -1]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:
                if L <= abs(A[i][j] - A[ni][nj]) <= R:
                    cnt += 1
                    visited[ni][nj] = True
                    lst.append((ni, nj))
                    total += A[ni][nj]
                    queue.append((ni, nj))
    length = len(lst)
    if length > 0:
        v = total // length
        for i, j in lst:
            A[i][j] = v

    return length

N, L, R = map(int, input().split())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ans = 0
while True:
    visited = [[False] * N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                res = bfs(i, j)
                result += res
    if result == 0:
        break
    ans += 1
print(ans)