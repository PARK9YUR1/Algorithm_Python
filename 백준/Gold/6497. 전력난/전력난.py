# 6497
import heapq

def BOJ6497(start):
    visited = [False] * m

    q = [(0, start)]
    result = 0

    while q:
        dist, home = heapq.heappop(q)

        if visited[home]:
            continue

        visited[home] = True
        result += dist

        for nxt, d in graph[home]:
            if not visited[nxt]:
                heapq.heappush(q, (d, nxt))

    return result


while True:
    m, n = map(int, input().split())  # 집의 수, 길의 수
    if m == n == 0:
        break

    graph = [[] for _ in range(m)]

    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())  # x번 집과 y번 집 사이 양방향 도로 거리 z미터
        graph[x].append((y, z))
        graph[y].append((x, z))
        total += z

    print(total - BOJ6497(0))