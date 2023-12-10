# 12761
# A B : 스카이콩콩 힘 / N 동규 M 주미 현재위치
from collections import deque
A, B, N, M = map(int, input().split())

def bfs(v):
    visited = [0]*100001
    q = deque([v])

    while q:
        x = q.popleft()
        if x == M:
            return visited[x]
        for u in [x-1, x+1, x-A, x+A, x-B, x+B, x*A, x*B]:
            if 0 <= u < 100001 and not visited[u]:
                visited[u] = visited[x] + 1
                q.append(u)

print(bfs(N))