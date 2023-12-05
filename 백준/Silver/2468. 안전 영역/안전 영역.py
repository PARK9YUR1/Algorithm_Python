# 2468
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0
for a in arr:
    mx = max(mx, max(a))

result = 0

def func(num):
    visited = [[False]*N for _ in range(N)]

    def bfs(i, j):
        nonlocal visited
        q = [(i, j)]
        visited[i][j] = True

        while q:
            x, y = q.pop(0)
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and arr[nx][ny] > num:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    res = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > num and visited[i][j] == False:
                bfs(i, j)
                res += 1

    return res

for n in range(mx+1):
    ans = func(n)
    result = max(ans, result)

print(result)