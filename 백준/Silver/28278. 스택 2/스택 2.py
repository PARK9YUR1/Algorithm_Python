import sys

N = int(input())  # 명령 수
stack = []
for _ in range(N):
    mr = list(map(int, sys.stdin.readline().split()))  # 명령 번호

    if mr[0] == 1:
        stack.append(mr[1])
    elif mr[0] == 2:
        if len(stack) > 0:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    elif mr[0] == 3:
        print(len(stack))
    elif mr[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif mr[0] == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)