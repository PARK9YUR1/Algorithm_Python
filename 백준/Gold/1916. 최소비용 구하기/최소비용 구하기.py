import heapq, sys
input = sys.stdin.readline

def mn_cost(start):
    min_heap = []
    heapq.heappush(min_heap, (0, start))
    c[start] = 0

    while min_heap:
        cst, cur_c = heapq.heappop(min_heap)
        if cur_c == E:
            break

        if c[cur_c] < cst:
            continue
        for nxt in graph[cur_c]:
            nxt_cn = nxt[0]
            new_c = cst + nxt[1]
            if c[nxt_cn] <= new_c:
                continue
            c[nxt_cn] = new_c
            heapq.heappush(min_heap, (new_c, nxt_cn))

N = int(input())  # 도시 개수
M = int(input())  # 버스 개수

graph = [[] for i in range(N+1)]
for _ in range(M):
    A, B, cost = map(int, input().split())
    graph[A].append((B, cost))
S, E = map(int, input().split())
c = [int(1e9)]*(N+1)

mn_cost(S)
print(c[E])

