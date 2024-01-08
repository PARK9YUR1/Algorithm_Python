def solution(rows, columns, queries):
    answer = []
    arr = [[0]*columns for _ in range(rows)]

    for query in queries:
        mn = rows*columns
        x1, y1, x2, y2 = query
        tmp = []
        
        x, y = x1-1, y1-1
        while y < y2-1:
            if not arr[x][y]:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            y += 1
                
        while x < x2-1:
            if not arr[x][y]:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            x += 1

        while y > y1-1:
            if not arr[x][y]:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            y -= 1

        while x >= x1:
            if not arr[x][y]:
                arr[x][y] = columns*x + (y+1)
            mn = min(mn, arr[x][y])
            tmp.append((x, y))
            x -= 1

        tmp = tmp[::-1]
        
        for i in range(len(tmp)-1):
            x, y = tmp[i]
            nx, ny = tmp[i+1]
            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
        
        answer.append(mn)

    for a in arr:
        print(a)
        
    return answer