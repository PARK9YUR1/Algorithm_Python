txt = input()
bomb = list(input())
N = len(bomb)
stack = []
for i in txt:
    stack.append(i)
    if len(stack) >= N:
        if stack[-N:] == bomb:
            for _ in range(N):
                stack.pop()

if len(stack) > 0:
    print(''.join(stack))
else:
    print('FRULA')