import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    dist = [int(1e9)]*(N+1)
    dist[start] = 0
    mn = [(0, start)]

    while mn:
        cur_dist, node = heapq.heappop(mn)
        if dist[node] < cur_dist:
            continue
        for nxt, time in graph[node]:
            new_dist = cur_dist + time
            if dist[nxt] > new_dist:
                dist[nxt] = new_dist
                heapq.heappush(mn, (new_dist, nxt))
    return dist

# N명, M개 단방향 도로, 집 -> X
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S, E, T = map(int, input().split())
    graph[S].append((E, T))

start_X = dijkstra(X)
mx = 0
for i in range(1, N+1):
    if i == X:
        continue
    arr = dijkstra(i)
    v = arr[X] + start_X[i]
    mx = max(mx, v)
print(mx)