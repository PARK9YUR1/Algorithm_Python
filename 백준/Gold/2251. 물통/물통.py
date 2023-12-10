# 2251
# 물통 부피 / A B 물통:비어있음 / C 물통:가득차있음.
A, B, C = map(int, input().split())
visited = [[False]*(B+1) for _ in range(A+1)]
result = []

def bfs(x, y):
    global visited
    q = [(x, y)]
    visited[x][y] = True

    while q:
        a, b = q.pop(0)
        c = C - a - b

        if a == 0 and c not in result:
            result.append(c)

        # A->B / A->C / B->A / B->C / C->A / C->B
        water = [min(a, B-b), min(a, C-c), min(b, A-a), min(b, C-c), min(c, A-a), min(c, B-b)]
        da = [-1, -1, 1, 0, 1, 0]
        db = [1, 0, -1, -1, 0, 1]
        for k in range(6):
            w = water[k]
            na, nb = a+da[k]*w, b+db[k]*w
            if visited[na][nb] == False:
                visited[na][nb] = True
                q.append((na, nb))

bfs(0, 0)
result.sort()
print(*result)