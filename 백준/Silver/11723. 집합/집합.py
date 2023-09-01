import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
    c = list(map(str, input().split()))
    if len(c) > 1:
        x = int(c[1])
    if c[0] == 'add' and x not in S:
        S.add(x)
    elif c[0] == 'remove' and x in S:
        S.remove(x)
    elif c[0] == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif c[0] == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif c[0] == 'all':
        S = {x+1 for x in range(20)}
    else:
        S = set()