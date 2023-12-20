# 14496
a, b = map(int, input().split())  # 바꾸려는 문자열
N, M = map(int, input().split())  # 전체 문자수, 치환 가능한 문자쌍 수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    visited = [0]*(N+1)
    visited[v] = 1
    q = [v]

    while q:
        x = q.pop(0)
        if x == b:
            return visited[x] - 1
        for u in graph[x]:
            if visited[u] == 0:
                visited[u] = visited[x] + 1
                q.append(u)
    return -1

print(bfs(a))