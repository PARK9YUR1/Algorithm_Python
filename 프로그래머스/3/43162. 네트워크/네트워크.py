def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:
                graph[i].append(j)
    
    visited = [False]*n
    
    def bfs(v):
        nonlocal visited
        q = [v]
        visited[v] = True
        
        while q:
            x = q.pop(0)
            for u in graph[x]:
                if not visited[u]:
                    q.append(u)
                    visited[u] = True
    
    for x in range(n):
        if not visited[x]:
            bfs(x)
            answer += 1
            
    return answer