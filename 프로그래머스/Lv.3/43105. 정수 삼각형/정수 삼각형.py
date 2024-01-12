def solution(triangle):
    N = len(triangle)
    DP = [[0] * i for i in range(1, N+1)]
    
    for i in range(N):
        for j in range(i+1):
            if i == 0:
                DP[i][j] = triangle[i][j]
            else:
                if j == 0:
                    DP[i][j] = DP[i-1][j] + triangle[i][j]
                elif j == i:
                    DP[i][j] = DP[i-1][j-1] + triangle[i][j]
                else:
                    DP[i][j] = max(DP[i-1][j-1] + triangle[i][j], DP[i - 1][j] + triangle[i][j])

    answer = max(DP[-1])
    return answer