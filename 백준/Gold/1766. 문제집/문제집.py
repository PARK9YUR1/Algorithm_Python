import heapq

N, M = map(int, input().split())  # 문제의 수, 정보개수

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
result = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    x = heapq.heappop(q)
    result.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

print(*result)