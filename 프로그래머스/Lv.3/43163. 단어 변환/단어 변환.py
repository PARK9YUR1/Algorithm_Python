def solution(begin, target, words):
    answer = 0
    words.insert(0, begin)
    N, W = len(words), len(begin)
    if target in words:
        idx = words.index(target)
        graph = [[] for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                arr = [words[i][k] != words[j][k] for k in range(W)]
                if sum(arr) == 1:
                    graph[i].append(j)
        
        def bfs(v):
            nonlocal answer
            q = [v]
            visited = [0]*N
            visited[v] = 1
            
            while q:
                x = q.pop(0)
                
                if x == idx:
                    answer = visited[x] - 1
                    return
                
                for u in graph[x]:
                    if not visited[u]:
                        q.append(u)
                        visited[u] = visited[x] + 1

        bfs(0)
        
    return answer