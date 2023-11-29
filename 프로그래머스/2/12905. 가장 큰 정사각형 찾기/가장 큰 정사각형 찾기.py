def solution(board):
    N, M = len(board), len(board[0])
    DP = [[0]*M for _ in range(N)]
    mx = 0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
            mx = max(mx, DP[i][j])

    return mx**2