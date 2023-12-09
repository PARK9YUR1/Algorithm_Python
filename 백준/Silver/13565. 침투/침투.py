# 13565
import sys
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]  # 0:흰색, 전류통함 / 1: 검은색, 전류안통함
visited = [[False]*N for _ in range(M)]

def dfs(x, y):
    global result
    visited[x][y] = True
    
    if x == M-1:
        result = 'YES'
        return
    
    for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0 and visited[nx][ny] == False:
            dfs(nx, ny)

result = 'NO'

for i in range(N):
    if result == 'YES':
        break
    if arr[0][i] == 0 and visited[0][i] == False:
        dfs(0, i)

print(result)