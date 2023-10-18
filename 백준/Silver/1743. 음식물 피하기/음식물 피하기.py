from collections import deque
import sys
input = sys.stdin.readline

def f(i, j):
    q = deque([])
    q.append((i, j))
    result = 1
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [0, 1], [1, 0], [0, -1], [-1, 0]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                result += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    return result

N, M, K = map(int, input().split())  # 세로, 가로, 음식물쓰레기 개수
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

mx = 0
for i in range(N):
    for j in range(M):
        ans = 0
        if arr[i][j] == 1:
            ans = f(i, j)
        mx = max(ans, mx)

print(mx)