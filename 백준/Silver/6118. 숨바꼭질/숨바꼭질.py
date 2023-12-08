# 6118
N, M = map(int, input().split())  # N:헛간개수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    q = [v]
    visited = [0]*(N+1)

    while q:
        x = q.pop(0)
        for u in graph[x]:
            if visited[u] == 0:
                visited[u] = visited[x] + 1
                q.append(u)

    return visited

res = bfs(1)
res[1] = 0
mx = max(res[2:])
a = res.index(mx)
b = mx
c = 0
for i in range(2, N+1):
    if res[i] == mx:
        c += 1
print(a, b, c)