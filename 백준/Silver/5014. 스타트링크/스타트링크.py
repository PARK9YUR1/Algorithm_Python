# 총 F층 / 스타트링크 위치 : G층 / 강호 위치 : S층
# U : 위층버튼, D : 아래층버튼
F, S, G, U, D = map(int, input().split())

def bfs(v):
    global visited
    q = [v]

    while q:
        x = q.pop(0)
        if x == G:
            return visited[x] - 1
        for u in graph[x]:
            if visited[u] == 0:
                visited[u] = visited[x] + 1
                q.append(u)

graph = [[] for _ in range(F+1)]
visited = [0] * (F+1)
visited[S] = 1

for i in range(1, F+1):
    if i+U <= F:
        graph[i].append(i+U)
    if i-D > 0:
        graph[i].append(i-D)

result = bfs(S)
if result == None:
    print('use the stairs')
else:
    print(result)