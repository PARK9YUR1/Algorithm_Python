# 12851
from collections import deque
N, K = map(int, input().split())  # N: 수빈 위치 / K: 동생 위치

def bfs(n):
    global result
    visited = [-1]*100001
    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        cur = q.popleft()
        if cur == K:
            result.append(visited[cur])
        for nxt in [cur-1, cur+1, 2*cur]:
            if 0 <= nxt <= 100000 and (visited[nxt] == -1 or visited[nxt] == visited[cur] + 1):
                visited[nxt] = visited[cur] + 1
                q.append(nxt)

result = []
bfs(N)
print(min(result))
print(len(result))
