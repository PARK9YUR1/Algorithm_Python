# 15686

def comb(n, r, s):
    global arr, dist
    if r == 0:
        total = 0
        for home in homes:
            hx, hy = home
            mn = 10**6
            for chicken in arr:
                cx, cy = chicken
                d = abs(hx-cx) + abs(hy-cy)
                mn = min(d, mn)
            total += mn
        dist.append(total)
        return

    for i in range(s, n-r+1):
        arr[r-1] = chickens[i]
        comb(n, r-1, i+1)


N, M = map(int, input().split())  # 도시크기 NxN, 남겨질 치킨집 수 M
city = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

length = len(chickens)
arr = [[] for _ in range(M)]
dist = []
comb(length, M, 0)
print(min(dist))