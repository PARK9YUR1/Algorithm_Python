N = int(input())
for i in range(1, N+1):
    print(' '*(N-i), end='')
    print('*', end='')
    if i == 1:
        print()
    else:
        print(' '*(2*(i-1)-1), end='')
        print('*')