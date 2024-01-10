N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    x = int(input())
    graph[i].append(x)

def bfs(v):
    q = [v]
    visited = [False]*(N+1)
    visited[v] = True

    while q:
        x = q.pop(0)
        for u in graph[x]:
            if not visited[u]:
                q.append(u)
                visited[u] = True

    return visited

arr = []
for i in range(1, N+1):
    visited = bfs(i)[1:]
    arr.append((i, sum(visited)))

arr.sort(key=lambda x:-x[1])
print(arr[0][0])