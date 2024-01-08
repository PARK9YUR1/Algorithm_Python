def solution(rows, columns, queries):
    
    answer = []
    arr = [[0]*columns for _ in range(rows)]
    
    # for i in range(len(queries)):
    #     print(f'===== {i} =====')
    #     if rows != 6: continue
    #     # if i != 0: continue
    #     query = queries[i]
        
    for query in queries:
        mn = rows*columns
        x1, y1, x2, y2 = query
        tmp = []
        
        x, y = x1-1, y1-1
        while y < y2-1:
            if arr[x][y]:
                pass
            else:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            y += 1
        # y -= 1
        # tmp.pop()
                
        while x < x2-1:
            if arr[x][y]:
                pass
            else:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            x += 1
        # x -= 1
        # tmp.pop()
        
        # print(y, y1)
        while y > y1-1:
            if arr[x][y]:
                pass
            else:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            y -= 1
        # y += 1
        # tmp.pop()
        
        while x >= x1:
            if arr[x][y]:
                pass
            else:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            x -= 1
        
        # print(tmp)
        tmp = tmp[::-1]
        
        # print('시계방향 돌기 전')
        # for a in arr:
        #     print(a)
        
        for i in range(len(tmp)-1):
            x, y = tmp[i]
            nx, ny = tmp[i+1]
            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
        
        answer.append(mn)
        
        # print('시계방향 돈 후')
    for a in arr:
        print(a)
        
    return answer