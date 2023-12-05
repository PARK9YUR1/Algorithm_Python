# 1389

N, M = map(int, input().split())  # N: 유저 수 / M: 친구 관계 수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    visited = [0] * (N+1)
    q = [v]

    while q:
        x = q.pop(0)
        for u in graph[x]:
            if visited[u] == 0:
                q.append(u)
                visited[u] = visited[x] + 1

    visited[v] = 0
    return visited

result = [0]*(N+1)
for i in range(1, N+1):
    result[i] = sum(bfs(i))

mn = min(result[1:])
print(result.index(mn))