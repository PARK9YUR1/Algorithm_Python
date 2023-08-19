import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    result = 'YES'
    stack = []
    txt = list(map(str, input()))
    cnt = -1
    for x in txt:
        cnt += 1
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                result = 'NO'
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                result = 'NO'
    if len(stack) > 0:
        result = 'NO'
    print(result)