import sys
input = sys.stdin.readline

N = int(input())  # 명령의 수
C = [list(map(str, input().split())) for _ in range(N)]
queue = []
for i in range(N):
    if C[i][0] == 'push':
        queue.append(C[i][1])
    elif C[i][0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            x = queue.pop(0)
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