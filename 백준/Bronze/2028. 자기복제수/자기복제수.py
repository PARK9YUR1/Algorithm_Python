T = int(input())
for _ in range(T):
    N = int(input())
    n = len(str(N**2)) - len(str(N))
    if str(N**2)[n:] == str(N):
        print('YES')
    else:
        print('NO')