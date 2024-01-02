def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    visited = [[False]*M for _ in range(N)]
    
    def bfs(i, j):
        nonlocal maps, N, M, visited, ans
        q = [(i, j)]
        visited[i][j] = True
        ans += int(maps[i][j])
        
        while q:
            x, y = q.pop(0)
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 'X' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    ans += int(maps[nx][ny])

    
    for i in range(N):
        for j in range(M):
            ans = 0
            if maps[i][j] != 'X' and visited[i][j] == False:
                bfs(i, j)
                answer.append(ans)
    
    if answer:
        answer.sort()
    else:
        answer = [-1]
    
    return answer