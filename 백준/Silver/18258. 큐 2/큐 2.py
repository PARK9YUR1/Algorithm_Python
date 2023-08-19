import sys
input = sys.stdin.readline
from collections import deque

N = int(input())  # 명령 수
queue = deque()

for _ in range(N):
    mr = list(map(str, input().split()))
    if mr[0] == 'push':
        x = int(mr[1])
        queue.append(x)
    elif mr[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            x = queue.popleft()
            print(x)
    elif mr[0] == 'size':
        print(len(queue))
    elif mr[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif mr[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif mr[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])