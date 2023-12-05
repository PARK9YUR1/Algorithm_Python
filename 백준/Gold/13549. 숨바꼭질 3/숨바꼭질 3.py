# 13549
from collections import deque
N, K = map(int, input().split())  # N: 수빈 위치 / K: 동생 위치

def bfs(n):
    visited = [0]*100001
    q = deque()
    q.append(n)

    while q:
        cur = q.popleft()
        if cur == K:
            return visited[cur]
        for nxt in [cur-1, cur+1, 2*cur]:
            if 0 <= nxt <= 100000 and visited[nxt] == 0:
                if nxt == 2*cur and nxt != 0:
                    visited[nxt] = visited[cur]
                    q.appendleft(nxt)
                else:
                    visited[nxt] = visited[cur] + 1
                    q.append(nxt)

print(bfs(N))