def solution(land):
    N = len(land)
    DP = [land[0] + [0]*3 for _ in range(N)]
    # DP = [[0]*4 for _ in range(N)]
    # DP[0] = land[0]
    
    answer = 0
    
    for i in range(1, N):
        DP[i][0] = max(DP[i-1][1], DP[i-1][2], DP[i-1][3]) + land[i][0]
        DP[i][1] = max(DP[i-1][0], DP[i-1][2], DP[i-1][3]) + land[i][1]
        DP[i][2] = max(DP[i-1][0], DP[i-1][1], DP[i-1][3]) + land[i][2]
        DP[i][3] = max(DP[i-1][0], DP[i-1][1], DP[i-1][2]) + land[i][3]
    
    mx = max(DP[i])
    
    return mx
