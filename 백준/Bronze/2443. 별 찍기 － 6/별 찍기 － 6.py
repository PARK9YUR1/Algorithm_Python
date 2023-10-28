N = int(input())
for i in range(N-1, -1, -1):
    j = 2 * (i+1) - 1
    k = N - (i+1)
    print(' '* k, end='')
    print('*' * j)