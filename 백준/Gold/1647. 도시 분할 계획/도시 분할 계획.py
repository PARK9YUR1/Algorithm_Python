import heapq, sys
input = sys.stdin.readline

def prim(start):
    visited = [False] * (N+1)
    min_heap = [(0, start)]
    MST = []

    while min_heap:
        cost, home = heapq.heappop(min_heap)
        if visited[home]:
            continue
        visited[home] = True
        MST.append((home, cost))
        for nxt, cost in graph[home]:
            if not visited[nxt]:
                heapq.heappush(min_heap, (cost, nxt))
    return MST

N, M = map(int, input().split())  # 집의 개수 N, 길의 개수 M
graph = [[] for _ in range(N+1)]
for _ in range(M):
    # A번 - B번 집 연결하는 유지비 C
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start = 1
MST = prim(start)

MST.sort(key=lambda x:x[1])
MST.pop()

total = 0
for home, cost in MST:
    total += cost
print(total)