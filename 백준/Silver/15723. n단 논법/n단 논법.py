# 15723
alpha, graph = [], []
N = int(input())
for _ in range(N):
    x, z, y = input().split()
    if x not in alpha:
        alpha.append(x)
        graph.append([])
    if y not in alpha:
        alpha.append(y)
        graph.append([])
    a = alpha.index(x)
    b = alpha.index(y)

    graph[a].append(b)

def dfs(v, x):
    global visited
    visited[v] = True
    if v == x:
        return
    for u in graph[v]:
        if visited[u] == False:
            dfs(u, x)

M = int(input())
for _ in range(M):
    x, z, y = input().split()
    if x not in alpha or y not in alpha:
        print('F')
        continue

    visited = [False]*len(alpha)
    a = alpha.index(x)
    b = alpha.index(y)
    dfs(a, b)

    if visited[b] == True:
        print('T')
    else:
        print('F')