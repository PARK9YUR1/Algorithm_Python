def solution(board):
    N, M = len(board), len(board[0])
    MN = min(N, M)
    visited = [[[False]*M for _ in range(N)] for _ in range(MN)]
    answer = 0
    
    
    def find(x, y, mn):
        nonlocal answer, visited
        cnt = 0
        
        for i in range(x, x+mn):
            for j in range(y, y+mn):
                if board[i][j] == 1:
                    cnt += 1
        
        if cnt == mn**2:
            answer = max(answer, cnt)
        else:
            for i in range(N):
                for j in range(M):
                    if i + mn-1 <= N and j + mn-1 <= M \
                    and mn > 1 and visited[mn-2][i][j] != True:
                        find(i, j, mn-1)
    
    for i in range(N):
        for j in range(M):
            if i + MN <= N and j + MN <= M and visited[MN-1][i][j] != True:
                find(i, j, MN)

    return answer