# 11060
N = int(input())
graph = [[] for _ in range(N)]
A = list(map(int, input().split()))
for i in range(N):
    if A[i] != 0:
        for j in range(i+1, i+1+A[i]):
            graph[i].append(j)

def bfs(v):
    visited = [0]*N
    q = [v]

    while q:
        x = q.pop(0)
        if x == N-1:
            return visited[x]
        for u in graph[x]:
            if u < N and visited[u] == 0:
                visited[u] = visited[x] + 1
                q.append(u)

res = bfs(0)
if res == None:
    res = -1
print(res)