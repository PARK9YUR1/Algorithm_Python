T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())  # k층 n호
    apt = [[0]*(n+1) for _ in range(k+1)]

    for i in range(k):
        for j in range(n+1):
            for l in range(j+1):
                if i == 0:
                    apt[i][j] = j
                apt[i+1][j] += apt[i][l]

    print(apt[k][n])