import heapq

def prim(start):
    visited = [False] * (V+1)
    min_heap = [(0, start)]
    MST = []

    while min_heap:
        w, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        MST.append((node, w))
        for nxt, w in graph[node]:
            if not visited[nxt]:
                heapq.heappush(min_heap, (w, nxt))
    return MST

V, E = map(int, input().split())  # 정점개수, 간선개수
graph = [[] for _ in range(V+1)]
for _ in range(E):
    # A번 정점 - B번 정점 => 가중치 C 간선 연결
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start = 1
MST = prim(start)

total = 0
for node, w in MST:
    total += w
print(total)