# 17144
R, C, T = map(int, input().split())
# -1:공기청정기 설치 / 나머지:미세먼지 양
arr = [list(map(int, input().split())) for _ in range(R)]


# 공기청정기 위치
c1, c2 = 0, 0  # 반시계, 시계
for r in range(R):
    if arr[r][0] == -1 and c1 == c2 == 0:
        c1, c2 = r, r+1


def dust():
    global arr
    dusts = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dusts.append((i, j, arr[i][j]))
    return dusts


def spread(dusts):
    global arr
    q = dusts

    while q:
        x, y, dust = q.pop()
        cnt = 0
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                arr[nx][ny] += dust//5
                cnt += 1
        arr[x][y] -= (dust//5) * cnt


# 반시계
def clean1():
    global arr
    v = 0
    for i in range(1, C):
        v, arr[c1][i] = arr[c1][i], v

    for i in range(c1-1, -1, -1):
        v, arr[i][C-1] = arr[i][C-1], v

    for i in range(C-2, -1, -1):
        v, arr[0][i] = arr[0][i], v

    for i in range(1, c1):
        v, arr[i][0] = arr[i][0], v


# 시계
def clean2():
    global arr
    v = 0
    for i in range(1, C):
        v, arr[c2][i] = arr[c2][i], v

    for i in range(c2+1, R):
        v, arr[i][C-1] = arr[i][C-1], v

    for i in range(C-2, -1, -1):
        v, arr[R-1][i] = arr[R-1][i], v

    for i in range(R-2, c2, -1):
        v, arr[i][0] = arr[i][0], v


t = 0
while t < T:
    # 먼지 찾기
    dusts = dust()
    # 미세먼지 확산 !
    spread(dusts)
    # 공기청정기 돌리기 !
    clean1()
    clean2()
    t += 1

# for a in arr:
#     print(a)

result = 2
for a in arr:
    result += sum(a)
print(result)