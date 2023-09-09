def dfs(v):
    global visited
    print(v, end=' ')
    visited[v] = True
    for u in graphs[v]:
        if visited[u] == True:
            continue
        dfs(u)

def bfs(v):
    global checked
    q = [v]
    checked[v] = True
    while q:
        x = q.pop(0)
        print(x, end=' ')
        for u in graphs[x]:
            if checked[u] == False:
                q.append(u)
                checked[u] = True
                
N, M, V = map(int, input().split())  # 정점개수 N, 간선개수 M, 탐색을 시작할 정점번호 V
graphs = [[] for _ in range(N + 1)]
visited = [False] * (N+1)
checked = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())  # 간선이 연결하는 두 정점번호
    graphs[a].append(b)
    graphs[b].append(a)

for graph in graphs:
    graph.sort()

dfs(V)
print()
bfs(V)