import sys
input = sys.stdin.readline

N = int(input())  # 명령의 수
C = [list(map(str, input().split())) for _ in range(N)]
stack = []
for i in range(N):
    if C[i][0] == 'push':
        stack.append(C[i][1])
    elif C[i][0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif C[i][0] == 'size':
        print(len(stack))
    elif C[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])