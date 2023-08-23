import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def bfs(r):
    global visited, cnt
    q = [r]
    result[r] = cnt
    visited[r] = True
    while q:
        x = q.pop(0)
        for i in graphs[x]:
            if visited[i] == True:
                continue
            cnt += 1
            result[i] = cnt
            visited[i] = True
            q.append(i)

# 정점 수, 간선 수, 시작정점
N, M, R = map(int, input().split())
adj = [i for _ in range(M) for i in list(map(int, input().split()))]
# adj = [int(x) for _ in range(M) for x in input().split()[:2]]

graphs = [[] for _ in range(N+1)]
for i in range(0, len(adj), 2):
    a, b = adj[i], adj[i+1]
    graphs[a].append(b)
    graphs[b].append(a)
visited = [False for _ in range(N+1)]
result = [0] * (N+1)

for g in graphs:
    g.sort()

cnt = 1
bfs(R)

for c in range(1, N+1):
    print(result[c])