import heapq

N, M = map(int, input().split())  # 정점개수, 간선수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())  # a와 b는 c의 가중치를 가짐
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(graph, start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        cur_cost, node = heapq.heappop(min_heap) 
        
        if cur_cost > dist[node]:
            continue

        for nxt, w in graph[node]:
            new_cost = cur_cost + w
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(min_heap, (new_cost, nxt))

    return dist

s, t = map(int, input().split())
D = dijkstra(graph, s)
print(D[t])