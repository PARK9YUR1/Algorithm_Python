def bfs(x):
    global visited
    q = [(x, 0)]
    for a in graph[x]:
        q.append((a, 1))
    visited[x] = True

    mx = 0
    while q:
        v, cnt = q.pop(0)
        for u in graph[v]:
            if visited[u] == False:
                mx = max(mx, cnt+1)
                q.append((u, cnt+1))
                visited[u] = True

    return mx

N = int(input())  # 회원 수
graph = [[] for _ in range(N+1)]
while True:
    A, B = map(int, input().split())
    if A == B == -1:
        break
    graph[A].append(B)
    graph[B].append(A)

mn = 10 ** 6
result = [mn]

for i in range(1, N+1):
    visited = [False] * (N+1)
    ans = bfs(i)
    mn = min(mn, ans)
    result.append(ans)

res = [mn, result.count(mn)]
for i in range(1, N+1):
    if result[i] == mn:
        res.append(i)

print(*res[:2])
print(*res[2:])