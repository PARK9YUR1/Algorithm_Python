import sys
input = sys.stdin.readline

def f(x):
    if x == N:
        total = [0]*5
        idx = []
        for i in range(N):
            if check[i] != 1:
                continue
            idx.append(i+1)
            for j in range(5):
                total[j] += arr[i][j]
        if total[0] >= mp and total[1] >= mf and total[2] >= ms and total[3] >= mv:
            result.append((total, idx))
        return

    check[x] = 1
    f(x+1)
    check[x] = 0
    f(x+1)


N = int(input())  # 식재료의 개수
# 단백질, 지방, 탄수화물, 비타민의 최소 영양성분
mp, mf, ms, mv = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = []
check = [0]*N
f(0)
if len(result) != 0:
    result.sort(key=lambda x:(x[0][4], x[1]))
    print(result[0][0][4])
    print(*result[0][1])
else:
    print(-1)