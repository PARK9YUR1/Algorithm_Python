import sys
input = sys.stdin.readline

M = int(input())  # 쿼리의 개수
hab = 0
xor = 0
for _ in range(M):
    lst = list(map(int, input().split()))
    if len(lst) == 2:
        if lst[0] == 1:
            hab += lst[1]
            xor ^= lst[1]
        elif lst[0] == 2:
            idx = 0
            hab -= lst[1]
            xor ^= lst[1]
    else:
        if lst[0] == 3:
            print(hab)
        elif lst[0] == 4:
            print(xor)
