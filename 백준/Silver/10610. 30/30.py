# 10610
N = list(map(int, input()))
N.sort(reverse=True)

if N[-1] == 0:
    if sum(N) % 3 == 0:
        print(''.join(map(str, N)))
    else:
        print(-1)
else:
    print(-1)