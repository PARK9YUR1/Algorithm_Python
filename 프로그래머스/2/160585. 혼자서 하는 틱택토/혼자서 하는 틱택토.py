def solution(board):
    answer = -1
    
    # 'O', 'X' 개수 찾기
    count_o = count_x = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                count_o += 1
            elif board[i][j] == 'X':
                count_x += 1
    
    dx = [0, 0, 1, -1, 1, -1, -1, 1]
    dy = [-1, 1, 0, 0, 1, -1, 1, -1]
    
    # 한방향으로만 이동하면서 한줄(3칸)이 되는지 확인
    def dfs(x, y, depth):
        nonlocal visited, answer, alpha, k

        nx, ny = x+dx[k], y+dy[k]

        if depth == 2:
            if visited[x][y] == 3:
                answer = 0
            return
        
        if 0 <= nx < 3 and 0 <= ny < 3 and board[nx][ny] == alpha:
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, depth+1)
                visited[nx][ny] = 0

    # X가 O보다 많을 때 : 무조건 불가능
    if count_o < count_x:
        answer = 0
    
    # O와 X의 개수가 같을 때
    elif count_o == count_x:
        # O가 한줄이 되지 않는 경우, 가능
        answer = 1
        # O가 한줄이 되는 경우, 불가능 (answer 갱신)
        visited = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O' and not visited[i][j]:
                    alpha = 'O'
                    for k in range(8):
                        visited[i][j] = 1
                        dfs(i, j, 0)
                        visited[i][j] = 0
    
    # O가 X보다 많을 때
    elif count_o > count_x:
        res = count_o - count_x
        # 차이가 1개일 때
        if res == 1:
            # X가 한줄이 되지 않는 경우, 가능
            answer = 1
            # X가 한줄이 되는 경우, 불가능 (answer 갱신)
            visited = [[0]*3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 'X' and not visited[i][j]:
                        alpha = 'X'
                        for k in range(8):
                            visited[i][j] = 1
                            dfs(i, j, 0)
                            visited[i][j] = 0
        # 개수가 2개 이상 : 불가능
        else:
            answer = 0
    
    return answer