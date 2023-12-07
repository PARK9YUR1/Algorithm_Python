# 2644
N = int(input())
graph = [[] for _ in range(N+1)]

A, B = map(int, input().split())
M = int(input())

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    q = [v]
    visited = [0]*(N+1)
    visited[v] = 1

    while q:
        x = q.pop(0)
        if x == B:
            return visited[x] - 1
        for u in graph[x]:
            if visited[u] == 0:
                visited[u] = visited[x] + 1
                q.append(u)

result = bfs(A)
if result == None:
    result = -1
print(result)