import heapq

def dijkstra(graph, start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        cur_cow, node = heapq.heappop(min_heap)

        if cur_cow > dist[node]:
            continue

        for nxt, cow in graph[node]:
            new_cow = cur_cow + cow
            if dist[nxt] > new_cow:
                dist[nxt] = new_cow
                heapq.heappush(min_heap, (new_cow, nxt))
                
    return dist[N]


N, M = map(int, input().split())  # N개의 헛간, m개의 소들의 길(양방향)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())  # 헛간 A B, 소 C 마리
    graph[A].append((B, C))
    graph[B].append((A, C))

start = 1
result = dijkstra(graph, start)
print(result)