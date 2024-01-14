import heapq

def solution(operations):
    q = []
    
    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        if oper == 'I':
            heapq.heappush(q, num)
        elif oper == 'D' and q:
            if num == -1:
                heapq.heappop(q)
            elif num == 1:
                q.pop()
    
    if q:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]
    
    return answer