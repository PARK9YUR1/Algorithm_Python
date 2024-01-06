N = int(input())  # 돌다리 돌 개수
A = list(map(int, input().split()))  # 점프할 수 있는 거리
S = int(input())  # 출발점

visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(N):
    graph[i+1].append(i+1 + A[i])
    graph[i+1].append(i+1 - A[i])
    

def bfs(v):
    global visited
    q = [v]
    visited[v] = 1

    while q:
        x = q.pop(0)
        for u in graph[x]:
            if 0 < u <= N and not visited[u]:
                q.append(u)
                visited[u] = 1

bfs(S)
print(sum(visited))
