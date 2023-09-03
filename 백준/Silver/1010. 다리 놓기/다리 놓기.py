T = int(input())
for _ in range(T):
    r, n = map(int, input().split())

    nCr = [[1] * i for i in range(1, n+2)]
    for i in range(2, n+1):
        for j in range(i+1):
            if j == 0 or i == j:
                nCr[i][j] = 1
            else:
                nCr[i][j] = nCr[i-1][j-1] + nCr[i-1][j]
    print(nCr[n][r])