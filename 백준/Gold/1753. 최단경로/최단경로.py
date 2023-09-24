import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    dist = [int(1e9)]*(V+1)
    dist[start] = 0
    mn = [(0, start)]

    while mn:
        cur_dist, node = heapq.heappop(mn)
        if cur_dist > dist[node]:
            continue
        for nxt, d in graph[node]:
            new_dist = cur_dist + d
            if dist[nxt] > new_dist:
                dist[nxt] = new_dist
                heapq.heappush(mn, (new_dist, nxt))
    return dist

V, E = map(int, input().split())  # 정점개수, 간선개수
K = int(input())  # 시작정점
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

arr = dijkstra(K)
for i in range(1, len(arr)):
    if arr[i] == int(1e9):
        print('INF')
        continue
    print(arr[i])