import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x):
    global visited, cnt
    lst[x] = cnt
    cnt += 1
    visited[x] = True
    for k in graphs[x]:
        if visited[k] == True:  # if visited[k] == False: dfs(k) 안됨
            continue
        dfs(k)


# 정점 수, 간선 수, 시작 정점
N, M, R = map(int, input().split())
adj = []
visited = [[False] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj.append((a, b))

graphs = [[] for _ in range(N+1)]
for i in range(len(adj)):
    u, v = adj[i]
    graphs[u].append(v)
    graphs[v].append(u)

for g in graphs:
    g.sort()

cnt = 1
lst = [0] * (N+1)
dfs(R)
for l in range(1, N+1):
    print(lst[l])