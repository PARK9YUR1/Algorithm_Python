# 11724
N, M = map(int, input().split())  # N:정점개수 / M:간선개수
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(v):
    global visited, cnt
    q = [v]
    visited[v] = True
    cnt += 1

    while q:
        x = q.pop(0)
        for u in graph[x]:
            if visited[u] == False:
                visited[u] = True
                q.append(u)

cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        bfs(i)
print(cnt)