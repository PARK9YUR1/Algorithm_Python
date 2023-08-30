from collections import deque
import sys
input = sys.stdin.readline

N = int(input())  # 명령의 수
C = [list(map(str, input().split())) for _ in range(N)]
queue = deque()
for i in range(N):
    if C[i][0] == 'push_front':
        queue.appendleft(C[i][1])
    elif C[i][0] == 'push_back':
        queue.append(C[i][1])
    elif C[i][0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            x = queue.popleft()
            print(x)
    elif C[i][0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            x = queue.pop()
            print(x)
    elif C[i][0] == 'size':
        print(len(queue))
    elif C[i][0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif C[i][0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])